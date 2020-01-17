import jieba
import requests
import wrapt
from celery import Celery
from celery.schedules import crontab
from gensim.models import KeyedVectors

# sys_argv = ''.join(sys.argv)
# if 'celery' in sys_argv:
#     jieba.enable_paddle()
#     model_file = '/Users/spaceship/Documents/Tencent_AILab_ChineseEmbedding_Min.txt'
#     tc_model = KeyedVectors.load_word2vec_format(model_file, binary=False)
#     with open('stopword.txt', 'r') as f:
#         USELESS = f.read().split('\n')
# else:
#     tc_model = None
#     USELESS = None
jieba.enable_paddle()
model_file = '/Users/spaceship/Documents/Tencent_AILab_ChineseEmbedding_Min.txt'
tc_model = KeyedVectors.load_word2vec_format(model_file, binary=False)
with open('stopword.txt', 'r') as f:
    USELESS = f.read().split('\n')


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        include=['tasks.tasks']
    )
    # celery.config_from_object('tasks.celeryconfig')
    celery.conf.beat_schedule = {
        # 'record_au_everyday': {
        #     'task': 'record_au_everyday',
        #     'schedule': crontab(hour=23, minute=30),
        #     'args': None,
        # },
        # 'record_statistics_route_crontab': {
        #     'task': 'record_statistics_route_crontab',
        #     'schedule': crontab(minute='*/10'),
        #     'args': None,
        # },
        'gen_nlp_keywords': {
            'task': 'gen_nlp_keywords',
            'schedule': crontab(minute='*/10'),
            'args': None,
        },
    }

    celery.conf.timezone = 'Asia/Shanghai'

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


@wrapt.decorator
def exception_handler(wrapped, instance, args, kwargs):
    task_name = wrapped.__name__
    try:
        res = wrapped(*args, **kwargs)
    except requests.Timeout as e:
        print(f'{task_name}执行失败, 原因:{str(e)}')
        return False
    except Exception as e:
        print(f'{task_name}执行失败, 原因:{str(e)}')
        return False
    else:
        print(f'{task_name}执行成功')
        print(res)
        return True
