from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to Yacine TV API"}

@router.get("/channels")
def get_channels():
    return {"channels": ["bein sport", "canal+", "yalla shoot"]}
