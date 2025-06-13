import redis
import os
import sys

import redis.exceptions

if len(sys.argv) < 2:
    print("Consumer name required")
    sys.exit(1)

CONSUMER_NAME = sys.argv[1]
print("Starting Consumer wth name ", CONSUMER_NAME)


r = redis.Redis(host='localhost' , port=6379, db=0, decode_responses=True)

try:
    r.ping()
    print("Redis connected")
except redis.ConnectionError as e:
    print("error in connecting redis")
    sys.exit(1)

STREAM_KEY = 'events'
GROUP_NAME="events_handlers"

try:
    r.xgroup_create(name=STREAM_KEY , groupname=GROUP_NAME, id="0-0", mkstream=True)
except redis.exceptions.ResponseError:
    pass


lastid = "0-0"
checkBackLog = True

while True:
    myid = lastid if checkBackLog else ">"

    result = r.xreadgroup(groupname=GROUP_NAME, consumername=CONSUMER_NAME, streams={STREAM_KEY: myid}, count=5 , block=2000)

    if not result:
        continue

    event_message = result[0][1]
    checkBackLog = not (len(event_message) == 0)

    for id , msg in event_message:
        print(f"Processing events with {id} and data : {msg}")
        r.xack(STREAM_KEY , GROUP_NAME, id)
        lastid = id
