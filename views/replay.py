from flask import Blueprint, request

from daos.replay import get_q_list

replay = Blueprint('replay', __name__)


@replay.route('/', methods=['GET'])
def get():
    """
    @api {get} /v1/replay/ 获取 智能回复
    @apiName GetQa
    @apiGroup 智能回复
    @apiDescription 获取智能回复
    @apiParam {str} s  问题
    @apiParam {int} n  返回最多几个答案，默认不传，为5
    @apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
    {
      "code": 0,  # 有答案为0，没有为101
      "data": {
        "res": [
          {
            "id": 2,
            "question": "外出和出差"
          }
        ],
        "sentence": "出差"
      },
      "message": "ok"  # 没答案为 "找不到答案，请换个方式提问!"
    }
    """
    s = request.args.get("s")
    n = request.args.get("n", 5)
    res = get_q_list(s, n)

    if res:
        return {
            'code': 0,
            'data': {
                'sentence': s,
                'res': res
            }

        }
    return {
        'code': 101,
        'message': '找不到答案，请换个方式提问!',
        'data': {
            'sentence': s,
        }

    }
