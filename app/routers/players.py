from fastapi import APIRouter

router = APIRouter()

@router.get("/players")
async def get_players():
    return 1