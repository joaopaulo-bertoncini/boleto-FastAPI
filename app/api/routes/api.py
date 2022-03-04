from fastapi import APIRouter

router = APIRouter()


@router.get("/alive")
def index():
    return {"ALIVE": "TRUE"}


router.include_router(router, tags=["alive"], prefix="/alive")
