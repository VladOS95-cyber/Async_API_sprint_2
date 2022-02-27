import backoff
from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError

es: AsyncElasticsearch | None = None


async def get_elastic() -> AsyncElasticsearch | None:
    return es


class ElasticStorage:

    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic

    @backoff.on_exception(backoff.expo,  ConnectionError, max_time=10)
    async def get_by_id(self, index, id, *args, **kwargs):
        try:
            return await self.elastic.get(index=index, id=id, *args, **kwargs)
        except NotFoundError:
            return None

    @backoff.on_exception(backoff.expo, ConnectionError, max_time=10)
    async def get_by_params(self, index, body, *args, **kwargs):
        try:
            return await self.elastic.search(index=index, body=body, *args, **kwargs)
        except NotFoundError:
            return None
