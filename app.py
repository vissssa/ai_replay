import public_config as config
from views.qa import qa

if config.SERVER_ENV != 'dev':
    from gevent import monkey

    monkey.patch_all()
else:
    pass

from library.api.tFlask import tflask


def create_app():
    app = tflask(config)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(qa, url_prefix="/v1/qa")


if __name__ == '__main__':
    create_app().run(port=config.PORT)
