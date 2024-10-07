from fastapi import APIRouter


router = APIRouter()

@router.post("/find")
async def find():
    return True
