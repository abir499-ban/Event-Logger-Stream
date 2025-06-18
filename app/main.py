from fastapi import FastAPI, status, Request, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import redis
import sys

r = redis.Redis(host='localhost' , port=6379, db=0, decode_responses=True)



@asynccontextmanager
async def server_lifeSpan(app : FastAPI):
    try:
        r.ping()
        print("Redis connected")
    except redis.ConnectionError as e:
        print("Redis failed to gett started")
        sys.exit(1)

    print("Server started")
    yield
    print("Server shutting down.......")

app = FastAPI(lifespan=server_lifeSpan)


@app.get('/')
async def sayHi():
    return JSONResponse(content= {'message' : "hello"}, status_code=status.HTTP_200_OK)


STREAM_KEY = 'events'

@app.post('/log_event', status_code=status.HTTP_202_ACCEPTED)
async def logevent(req : Request):
    event_data = await req.json()
    try:
        print(event_data)
        r.xadd(STREAM_KEY , event_data, maxlen=1000)
        print("Event appended to stream")
        return JSONResponse(content={'message' : 'Event Logged'})
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="some error occured")

