from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/events",
    tags=["events"]
)


@router.get("/")
async def list_events():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'list_events'
    })
    return JSONResponse(content=data)


@router.get("/{event_id}")
async def show_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_event'
    })
    return JSONResponse(content=data)


@router.post("")
async def create_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'create_event'
    })
    return JSONResponse(content=data)


@router.put("/{event_id}")
async def update_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'update_event'
    })
    return JSONResponse(content=data)


@router.delete("/{event_id}")
async def delete_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'delete_event'
    })
    return JSONResponse(content=data)


@router.get("/{event_id}/users/{nickname}")
async def get_event_user():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'get_event_user'
    })
    return JSONResponse(content=data)
