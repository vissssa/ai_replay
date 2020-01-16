from jaeger_client import Config
from opentracing_instrumentation.client_hooks import install_patches

from local_config import JAEGER_HOST


def init_tracer(service):
    # 只追踪这几个服务
    install_patches(
        [
            'opentracing_instrumentation.client_hooks.urllib.install_patches',
            'opentracing_instrumentation.client_hooks.urllib2.install_patches',
            'opentracing_instrumentation.client_hooks.mysqldb.install_patches',
            'opentracing_instrumentation.client_hooks.requests.install_patches',
            'opentracing_instrumentation.client_hooks.sqlalchemy.install_patches',
        ]
    )

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            # 'logging': True,
            'local_agent': {
                'reporting_host': JAEGER_HOST,
                # 'reporting_port': JAEGER_PORT
            },
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()
