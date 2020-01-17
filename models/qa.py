from library.api.db import EntityModel, db

"""
默认情况flask_migrate不会检测数据类型和长度的变化
需要找到migrations/env.py文件，在run_migrations_online函数加入如下内容:
context.configure(
          …………
          compare_type=True,  # 检查字段类型
          compare_server_default=True # 比较默认值
          )
"""


class Qa(EntityModel):
    ACTIVE = 0  # 状态 0是存在，1是删除
    DISABLE = 1
    NO_SEG = 0  # 切分状态 0是未切分，1是切分了
    SEG = 1

    question = db.Column(db.String(200))  # 问题
    answer = db.Column(db.Text())  # 答案
    keywords = db.Column(db.String(200))  # 用户填写的关键词
    nlp_keywords = db.Column(db.String(200))  # nlp猜测的相关关键词
    status = db.Column(db.Integer, default=ACTIVE)  # 状态
    has_seg = db.Column(db.Integer, default=NO_SEG)  # 切分状态
    hot = db.Column(db.Integer, default=0)  # 热度。随着被点击增大


def qa_query():
    return Qa.query.add_columns(
        Qa.id,
        Qa.question,
        Qa.answer,
        Qa.keywords,
        Qa.nlp_keywords,
        Qa.status,
        Qa.has_seg,
        Qa.hot
    )
# class KeyWords(EntityModel):
#     pass
#
#
# class QaKeyWord(EntityModel):
#     qa_id = db.Column(db.Integer)
#     kw_id = db.Column(db.Integer)
