import datetime
from fastapi import HTTPException
import asyncio
from models.models import QueryModel, Comment
from functools import wraps
from crud.create import add_user
from config.database_connection import manager

def outline(func):

    @wraps(func)
    async def wrapper(jsn: QueryModel, backdoor=None, *args, **kwargs):
        try:
            text = jsn.text
            created_at =  datetime.datetime.utcnow().isoformat()
            if 'хорош' in text or 'люблю' in text:
                sentiment = 'positive'
            elif 'плохо' in text or 'ненавиж' in text:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
        except:
            return HTTPException(400)
        id, session = (add_user(Comment(text=text, created_at=created_at, sentiment=sentiment), manager))
        session.close()
        return await func(jsn, backdoor={"id":id, "text":text, "created_at":created_at, "sentiment":sentiment}, *args, **kwargs)
    return wrapper

