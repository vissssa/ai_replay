import jieba
from sqlalchemy import or_, desc

from library.api.render import row2list
from models.qa import qa_query, Qa
from tasks.extentions import USELESS, tc_model
from tasks.tasks import in_model


def _get_similar_words(s):
    seg_words = jieba.cut(s, use_paddle=True)
    res_list = []
    for word in seg_words:
        if word not in USELESS:
            res_list.append(word)
            if in_model(word):
                sim_list = tc_model.similar_by_word(word, topn=10)
                res_list.extend([i[0] for i in sim_list])
    return res_list


def get_q_by_word(word, n):
    if not 0 < n < 10:
        n = 5
    row = qa_query().filter(
        Qa.nlp_keywords.like(f'%{word}%'),
        Qa.status == Qa.ACTIVE
    ).order_by(desc(Qa.hot)).limit(n).all()
    return row2list(row)


def get_q_list(s, n):
    if not s:
        return
    res_list = _get_similar_words(s)
    used = []
    res = []
    for word in res_list:
        q_list = get_q_by_word(word, n)
        for q in q_list:
            if q['id'] not in used:
                res.append({'id': q['id'], 'question': q['question'], 'hot': q['hot']})
                used.append(q['id'])
    return res
