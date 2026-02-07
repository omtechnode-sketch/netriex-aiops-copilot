import redis
from rq import Queue
from app.config.settings import settings

redis_conn = redis.Redis.from_url(settings.REDIS_URL)

event_queue = Queue("events", connection=redis_conn)
