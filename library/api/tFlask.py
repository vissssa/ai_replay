from flask import Flask, jsonify
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from library.api.db import db
from library.api.exceptions import Error
from library.api.parse import format_response
# from library.api.tMiddleware import t_middleware
from library.tlogger import logger_create

# from flask_opentracing import FlaskTracing
# from library.api.db import cache

try:
    from public_config import SERVER_ENV
except ImportError:
    SERVER_ENV = 'product'


class TFlask(Flask):

    def make_response(self, rv):
        if isinstance(rv, dict):
            rv = jsonify(format_response(rv))
        return super().make_response(rv)

    def run(self, host='0.0.0.0', port=5000, debug=True, workers=None, load_dotenv=True, server_env=None, **options):
        if server_env == 'dev' or SERVER_ENV == 'dev':
            super().run(host=host, port=port, debug=debug)
        else:
            import multiprocessing
            from gunicorn.app.base import BaseApplication

            class Application(BaseApplication):

                def __init__(self, app, local_options=None):
                    self.options = local_options or {}
                    self.application = app
                    super(Application, self).__init__()

                def load_config(self):
                    config = dict([(key, value) for key, value in self.options.items()
                                   if key in self.cfg.settings and value is not None])
                    for key, value in config.items():
                        self.cfg.set(key.lower(), value)

                def load(self):
                    return self.application

                def init(self, parser, opts, args):
                    super(Application, self).init(parser, opts, args)

            current_options = {
                'bind': f'{host}:{port}',
                'workers': workers or (multiprocessing.cpu_count() * 2) + 1,
                'worker_class': 'gevent',
                'timeout': '1800',
            }

            Application(self, current_options).run()


def register_logger(app, config):
    logger_create(config.SERVICE_NAME, app)


def register_extensions(app):
    db.init_app(app)
    # cache.init_app(app)
    Migrate(app, db)


def register_tracing(app, config):
    # jaeger_tracer = init_tracer(config.SERVICE_NAME)
    # FlaskTracing(tracer=jaeger_tracer, trace_all_requests=True, app=app)
    pass


WARN_CODE = (108, 109, 110, 412)


def register_exception(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        if isinstance(e, HTTPException):
            code = e.code
            message = e.name
        elif issubclass(type(e), Error):
            code = e.code
            message = e.message
        else:
            code = 500
            message = "服务异常，请联系管理员"

        err_res = {
            "code": code,
            "message": message
        }
        # 操作限制以及未登录
        if code in WARN_CODE:
            app.logger.warn('')
        else:
            app.logger.error('')
        return format_response(err_res)


def tflask(config):
    app = TFlask(config.SERVICE_NAME)
    # 只为注入mysql链接，使用config中内容没有使用current_app.config
    app.config.from_object(config)
    # t_middleware(app)
    register_logger(app, config)
    # register_tracing(app, config)
    register_extensions(app)

    register_exception(app)
    return app
