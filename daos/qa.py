from sqlalchemy import desc

from library.api.db import db
from library.api.exceptions import CannotFindObjectException
from library.api.render import row2list
from models.qa import Qa, qa_query


def keyword2list(data):
    keywords = data['keywords']
    nlp_keywords = data['nlp_keywords']

    data['keywords'] = keywords.split(',') if keywords is not None and len(keywords) > 0 else []
    data['nlp_keywords'] = nlp_keywords.split(',') if nlp_keywords is not None and len(nlp_keywords) > 0 else []


def get_qa(page_size, page_index):
    query = qa_query().order_by(desc(Qa.id))
    count = query.count()
    if page_size and page_index:
        query = query.limit(int(page_size)).offset((int(page_index) - 1) * int(page_size))
    data = row2list(query.all(), exclude=['status', 'has_seg'], func=keyword2list)

    return count, data


def get_qa_by_id(qa_id):
    qa_row = qa_query().filter_by(id=qa_id).all()
    if qa_row:
        return row2list(qa_row, exclude=['status', 'has_seg'], func=keyword2list)
    else:
        raise CannotFindObjectException('未找到当前问答')


def create_qa(post_form):
    post_form['keywords'] = ','.join(post_form['keywords'])
    query = Qa(**post_form)
    with db.auto_commit():
        db.session.add(query)
    return 0


def modify_qa(post_form):
    qa_id = post_form['id']
    if not isinstance(post_form['id'], int):
        raise CannotFindObjectException
    post_form.pop('id')

    qa_row = Qa.query.get(qa_id)
    if not qa_row:
        raise CannotFindObjectException

    # 每次修改后都置为未nlp状态
    post_form['has_seg'] = 0
    with db.auto_commit():
        qa_row.query.filter_by(id=qa_id).update(post_form)
    return 0


def delete_qa(qa_id):
    qa_row = Qa.query.get(qa_id)
    if qa_row is None:
        raise CannotFindObjectException

    qa_row.status = qa_row.DISABLE
    db.session.add(qa_row)
    db.session.commit()
    return 0
