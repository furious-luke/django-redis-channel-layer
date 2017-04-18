from asgi_redis.core import RedisChannelLayer
from django_redis import get_redis_connection


class DjangoRedisChannelLayer(RedisChannelLayer):
    def _generate_connections(self, **redis_kwargs):
            return [get_redis_connection()]
