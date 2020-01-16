try:
    from local_config import *
except ImportError:
    pass
SESSION_TIME = 14 * 24 * 60 * 60
AUTH_KEY = 'Authorization'

PROJECT_NAME = 'ai_replay'
SERVICE_NAME = 'ai_replay'

PORT = 5000

SQLALCHEMY_TRACK_MODIFICATIONS = True
SCHEDULER_API_ENABLED = True

MSG_MAP = {
    0: 'ok',

    101: 'can not find object',
    102: 'save object error',
    103: '标题或名称重复',
    104: 'can not create object',
    105: 'remove failed',
    106: 'operate failed',
    108: 'permission denied',
    109: 'project permission denied',
    110: '无此操作权限，请联系管理员',

    201: 'field required',
    202: 'field length error',

    301: 'password wrong',
    303: 'username or password wrong',

    403: 'not allowed',
    404: 'not found',
    410: 'auth expired',
    411: 'auth error',
    412: 'not login',
    413: 'username is not exist or password error',
    414: 'invalid data',
}

ISOTIMEFORMAT = '%Y-%m-%d %X'

# gateway未启用前暂用

TCLOUD_FILE_TEMP_PATH = '/tmp/ai_replay'
