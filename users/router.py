from fastapi import APIRouter, Depends
from typing import List
from starlette.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from databases import Database
from .models import User
from .schema import UserSchema
from utils.dbutils import get_connection
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        decoded_token = auth.verify_id_token(cred.credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    user = decoded_token['firebase']['identities']
    return user


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("", response_model=List[UserSchema])
async def list_users(current_user=Depends(get_current_user), database: Database = Depends(get_connection)):
    users = User().__table__
    query = users.select()
    return await database.fetch_all(query)


@router.get("/{nickname}")
async def show_user(current_user=Depends(get_current_user)):
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_user'
    })
    return JSONResponse(content=data)


@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_user'
    })
    return JSONResponse(content=data)


@router.post("/me")
async def create_me(current_user=Depends(get_current_user)):
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'create_user'
    })
    return JSONResponse(content=data)


@router.put("/me")
async def update_me(current_user=Depends(get_current_user)):
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'update_user'
    })
    return JSONResponse(content=data)


@router.delete("/me")
async def delete_me(current_user=Depends(get_current_user)):
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'delete_user'
    })
    return JSONResponse(content=data)
