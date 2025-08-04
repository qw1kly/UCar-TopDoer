from fastapi import APIRouter

from models.models import QueryModel
from utils import outline

router = APIRouter()


@router.post("/reviews")
@outline
async def comment(jsn: QueryModel, backdoor = None):
    return backdoor

