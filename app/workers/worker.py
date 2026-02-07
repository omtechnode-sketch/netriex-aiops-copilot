import redis
from rq import Worker, Queue
from app.config.settings import settings

redis_conn = redis.Redis.from_url(settings.REDIS_URL)

def start_worker():
    queue = Queue("events", connection=redis_conn)
    worker = Worker([queue], connection=redis_conn)
    worker.work()

if __name__ == "__main__":
    start_worker()
