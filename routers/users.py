from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def list_users():
    pass


@router.get("/users/{nickname}")
async def show_user():
    pass


@router.post("/users")
async def create_user():
    pass


@router.put("/users/{nickname}")
async def update_user():
    pass


@router.delete("/users/{nickname}")
async def delete_user():
    pass