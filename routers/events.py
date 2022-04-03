from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/events", tags=["events"])
async def list_events():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'list_events'
    })
    return JSONResponse(content=data)


@router.get("/events/{event_id}", tags=["events"])
async def show_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'show_event'
    })
    return JSONResponse(content=data)


@router.post("/events", tags=["events"])
async def create_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'create_event'
    })
    return JSONResponse(content=data)


@router.put("/events/{event_id}", tags=["events"])
async def update_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'update_event'
    })
    return JSONResponse(content=data)


@router.delete("/events/{event_id}", tags=["events"])
async def delete_event():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'delete_event'
    })
    return JSONResponse(content=data)
