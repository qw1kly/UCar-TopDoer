from fastapi import APIRouter, Request, HTTPException

from crud.read import get_data
from models.models import Comment
from config.database_connection import manager

router = APIRouter()

@router.get("/reviews")
async def getter(request: Request):
    params = dict(request.query_params)

    if params.get("sentiment") and params["sentiment"] == 'negative':
        return get_data(Comment, manager)
    return HTTPException(405)