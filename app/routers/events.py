from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
async def get_events():
    return 1