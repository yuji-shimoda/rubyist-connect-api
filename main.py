from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from users.router import router as userrouter
from starlette.requests import Request
from mangum import Mangum
from database import database
from pydantic import BaseSettings, BaseModel
from logging import getLogger

logger = getLogger(__name__)


class Settings(BaseSettings):
    base_path: str = ""


settings = Settings()


def create_app():
    app = FastAPI(
        title='Rubyist Connect API',
        servers=[{"url": settings.base_path}],
        root_path=settings.base_path,
    )
    return app


app = create_app()
app.include_router(userrouter)
#app.include_router(events.router, tags=['events'])

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response

handler = Mangum(app)
