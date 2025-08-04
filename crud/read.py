from models.models import Comment


def get_data(comm: Comment, session_):
    session_.open()
    session = session_.session
    comments = session.query(comm).all()

    sdv = []

    for i in range(len(comments)):
        if comments[i].sentiment == 'negative':
            sdv.append(comments[i])
    session_.close()
    return sdv