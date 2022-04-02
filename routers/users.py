from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/users", tags=["users"])
async def list_users():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'list_users'
    })
    return JSONResponse(content=data)


@router.get("/users/{nickname}", tags=["users"])
async def show_user():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_user'
    })
    return JSONResponse(content=data)


@router.post("/users", tags=["users"])
async def create_user():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'create_user'
    })
    return JSONResponse(content=data)


@router.put("/users/{nickname}", tags=["users"])
async def update_user():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'update_user'
    })
    return JSONResponse(content=data)


@router.delete("/users/{nickname}", tags=["users"])
async def delete_user():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'delete_user'
    })
    return JSONResponse(content=data)
