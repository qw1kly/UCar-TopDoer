from models.models import Comment

def add_user(comm: Comment, session_):
    session_.open()
    session = session_.session
    session.add(comm)
    session.commit()
    return comm.id, session_