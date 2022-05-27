# admin path operations shared between several projects.
# we cannot modify it and add a prefix, dependencies, tags, etc. directly to the APIRouter
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}