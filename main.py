from fastapi import FastAPI
import redis
import os
import time

app = FastAPI()

REDIS_URL = os.environ.get("REDIS_URL")
r = redis.from_url(REDIS_URL, decode_responses=True)


@app.get("/")
def root():
    return {"status": "roblox farm controller online"}


@app.post("/worker/register")
def register_worker(worker_id: str):
    r.hset("workers", worker_id, int(time.time()))
    return {"status": "registered", "worker": worker_id}


@app.post("/worker/heartbeat")
def heartbeat(worker_id: str):
    r.hset("workers", worker_id, int(time.time()))
    return {"status": "ok"}


@app.get("/workers")
def list_workers():
    return r.hgetall("workers")
