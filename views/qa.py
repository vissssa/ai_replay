from flask import Blueprint, request

from daos.qa import create_qa, modify_qa, get_qa, get_qa_by_id, delete_qa
from library.api.extentions import validation, parse_json_formdict

qa = Blueprint('qa', __name__)


@qa.route('/', methods=['GET'])
def get():
    """
    @api {get} /v1/qa/ 获取 qa数据
    @apiName GetQa
    @apiGroup 智能回复
    @apiDescription 获取qa数据（分页）
    @apiParam {int} page_size  page_size
    @apiParam {int} page_index  page_index
    @apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
    {
      "code": 0,
      "data": [
        {
          "answer": "每年 8 月启动晋升评估，9 月 1 日生效",
          "id": 1,
          "keywords": [],
          "nlp_keywords": [],
          "question": "晋升窗口期"
        }
      ],
      "message": "ok",
      "page_index": "1",
      "page_size": "10",
      "total": 1
    }
    """
    page_size = request.args.get('page_size')
    page_index = request.args.get('page_index')
    count, data = get_qa(page_size, page_index)
    return {'code': 0, 'data': data, 'total': count, 'page_index': page_index, 'page_size': page_size}


@qa.route('/<int:qa_id>', methods=['GET'])
def get_by_id(qa_id):
    """
    @api {get} /v1/qa/{qa_id} 获取 qa数据通过qa id
    @apiName GetQaById
    @apiGroup 智能回复
    @apiDescription 通过qa id获取qa数据
    @apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
    {
      "code": 0,
      "data": [
        {
          "answer": "每年 8 月启动晋升评估，9 月 1 日生效",
          "id": 1,
          "keywords": [],
          "nlp_keywords": [],
          "question": "晋升窗口期"
        }
      ],
      "message": "ok",
    }
    """
    data = get_qa_by_id(qa_id)
    return {'data': data}


@qa.route('/', methods=['POST'])
@validation('qa_modify')
def post():
    """
    @api {post} /v1/qa/ 新增和修改qa数据
    @apiName ModifyQa
    @apiGroup 智能回复
    @apiDescription 新增和修改qa数据, 通过是否携带id
    @apiParamExample {json} Request-Example:
    {
        "id": 1,  # 当不携带id时就是新增，反之就是修改
        "question": "晋升窗口期",
        "answer": "每年 8 月启动晋升评估，9 月 1 日生效",
        "keywords": ["晋升"]
    }
    @apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
    {
      "code": 0,
      "data": [],
      "message": "ok",
    }
    """
    post_form = parse_json_formdict('qa_modify')
    if post_form['id'] is not None:
        code = modify_qa(post_form)
    else:
        code = create_qa(post_form)
    return {'code': code}


@qa.route('/<int:qa_id>', methods=['DELETE'])
def delete(qa_id):
    """
    @api {delete} /v1/qa/{qa_id} 删除qa
    @apiName DeleteQa
    @apiGroup 智能回复
    @apiDescription 通过id删除Qa
    @apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
    {
      "code": 0,
      "data": [],
      "message": "ok",
    }
    """
    code = delete_qa(qa_id)
    return {'code': code}
