import logging

import aioredis
import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import film, genre, person
from core import config
from core.logger import LOGGING
from db import elastic_db, redis_db
from services.person import PersonService
from services.genre import GenreService
from services.film import FilmService

logging.getLogger('backoff').addHandler(logging.StreamHandler())



app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    description='Information about movies, genres and persons involved in movie making',
    version='1.0.0'
)


@app.on_event('startup')
async def startup():
    elastic_db.es = AsyncElasticsearch(hosts=f'{config.ELASTIC_HOST}:{config.ELASTIC_PORT}')
    redis_db.redis = await aioredis.create_redis(address=f'redis://{config.REDIS_HOST}:{config.REDIS_PORT}')

    #проверка валидации сервисов
    FilmService(elastic_db.es, redis_db.redis)
    PersonService(elastic_db.es, redis_db.redis)
    GenreService(elastic_db.es, redis_db.redis)


@app.on_event('shutdown')
async def shutdown():
    await elastic_db.es.close()
    redis_db.redis.close()
    await redis_db.redis.wait_closed()

app.include_router(film.router, prefix='/api/v1/film', tags=['film'])
app.include_router(genre.router, prefix='/api/v1/genre', tags=['genre'])
app.include_router(person.router, prefix='/api/v1/person', tags=['person'])


if __name__ == '__main__':

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
