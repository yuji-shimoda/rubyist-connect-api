from fastapi import FastAPI
from routers import user
from mangum import Mangum
from logging import getLogger
logger = getLogger(__name__)

app = FastAPI(
    title='Rubyist Connect API',
    openapi_prefix='/dev'
)
app.include_router(user.router)

handler = Mangum(app)
