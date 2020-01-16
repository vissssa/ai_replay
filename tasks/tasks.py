import jieba

from library.api.db import db
from models.qa import qa_query, Qa
from tasks import celery
from tasks.extentions import exception_handler, USELESS, tc_model


def in_model(word):
    if word is None or len(word) == 0 or word not in tc_model.vocab:
        return False
    else:
        return True


@celery.task(name='gen_nlp_keywords')
@exception_handler
def gen_nlp_keywords():
    rows = qa_query().filter_by(has_seg=Qa.NO_SEG, status=Qa.ACTIVE)
    query_list = []
    for row in rows:
        nlp_keywords = []
        keywords = row.keywords
        seg_words = keywords.split(',') if keywords is not None and len(keywords) > 0 else []
        if len(seg_words) == 0:
            seg_words = jieba.cut(row.question)
        for w in seg_words:
            if w not in USELESS:
                nlp_keywords.append(w)
                if in_model(w):
                    sim_list = tc_model.similar_by_word(w, topn=10)
                    nlp_keywords.extend([i[0] for i in sim_list])
        query = Qa.query.get(row.id)
        query.nlp_keywords = ','.join(nlp_keywords)
        query.has_seg = Qa.SEG
        query_list.append(query)
    db.session.add_all(query_list)
    db.session.commit()
    return True

    #
    # rows = qa_query().filter_by(has_seg=Qa.NO_SEG).all()
    # nlp_keywords = []
    # for row in rows:
    #     keywords = row.keywords
    #     row.keywords = keywords.split(',') if keywords is not None and len(keywords) > 0 else []
    #     if len(row.keywords) == 0:
    #         seg_words = jieba.cut(row.question, use_paddle=True)
    #     else:
    #         seg_words = row.keywords
    #     for w in seg_words:
    #         if w not in USELESS:
    #             nlp_keywords.append(w)
    #             if in_model(w):
    #                 sim_list = tc_model.similar_by_word(w, topn=10)
    #                 nlp_keywords.extend([i[0] for i in sim_list])
    #     row.nlp_keywords = ','.join(nlp_keywords)
    # db.session.add(rows)
    # db.session.commit()
