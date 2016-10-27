# django-redis-channel-layer

Makes Django Channels `asgi_redis` channel layer use the same connection pool
as `django-redis`. This helps to maintain control over the number of Redis
connections.


## Installation

There is currently no pip package, so the long-winded form is needed:

```bash
pip install -e -e git+https://github.com/furious-luke/django-redis-channel-layer#egg=django-redis-channel-layer
```


## Usage

Simply replace your channel layer in `settings.py`:

```python
REDIS_URL = 'redis://your-redis-url'

CHANNEL_LAYERS = {
    'default': {
        ...
        'BACKEND': 'redis_channel_layer.DjangoRedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        }
        ...
    }
}
```
