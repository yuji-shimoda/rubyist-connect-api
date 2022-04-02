from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from routers import users
from mangum import Mangum
from logging import getLogger
from pydantic import BaseSettings, BaseModel
logger = getLogger(__name__)


class Item(BaseModel):
    statusCode: int


class Settings(BaseSettings):
    base_path: str = "/dev"


settings = Settings()


def create_app():
    app = FastAPI(
        title='Rubyist Connect API',
        servers=[{"url": settings.base_path}],
        root_path=settings.base_path,
    )
    return app


app = create_app()
app.include_router(users.router)


@app.get("/")
async def root():
    data = jsonable_encoder({
        'statusCode': 200,
        'name': 'root'
    })
    return JSONResponse(content=data)

handler = Mangum(app)
