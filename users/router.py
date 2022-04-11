from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from databases import Database
from .models import User
from .schema import UserSchema
from utils.dbutils import get_connection

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("", response_model=List[UserSchema])
async def list_users(request: Request, database: Database = Depends(get_connection)):
    users = User().__table__
    query = users.select()
    return await database.fetch_all(query)


@router.get("/{nickname}")
async def show_user():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_user'
    })
    return JSONResponse(content=data)


@router.get("/me")
async def show_me():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_user'
    })
    return JSONResponse(content=data)


@router.post("/me")
async def create_me():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'create_user'
    })
    return JSONResponse(content=data)


@router.put("/me")
async def update_me():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'update_user'
    })
    return JSONResponse(content=data)


@router.delete("/me")
async def delete_me():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'delete_user'
    })
    return JSONResponse(content=data)
