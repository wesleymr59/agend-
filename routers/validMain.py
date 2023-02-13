from fastapi import APIRouter

router = APIRouter( prefix="/hello",
    tags=["hello"],
    responses={404: {"description": "Not found"}},)

@router.get("", tags=["hello"])
async def hello():
    return {"Message": "Hellow"}