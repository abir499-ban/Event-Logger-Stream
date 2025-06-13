# Redis Stream Event Logger

A simple mini project to illustrate the use of **Redis Streams** and **consumer groups** with Python and FastAPI.  
This project shows how to log events to a Redis stream via a FastAPI backend and process them with multiple consumers, demonstrating load balancing, backlog handling, and stream trimming.

---

## Features

- **Event Producer:** FastAPI server exposes an endpoint to log events to a Redis stream.
- **Event Consumers:** Standalone Python scripts process events from the stream using Redis consumer groups.
- **Dynamic Consumer Names:** Run multiple consumers with unique names to see load balancing in action.
- **Backlog Handling:** Demonstrates how pending (unacknowledged) messages are processed after consumer restarts.
- **Stream Trimming:** (Optional) Keep your stream size in check with manual or automatic trimming.

---

## Project Structure
your_project/
├── app/
│ └── main.py # FastAPI producer (event logger)
├── consumer.py # Event consumer script
├── requirements.txt # Python dependencies
├── README.md # Project documentation

----------------
## Some points about Redis Streams:
- Redis Streams help to continuosuly stream enormous amount of data 
to multiple consumers where the inflow rate ( per milisecond) of data in pretty high.
- The multiple consumer can habe various jobs like one can has to update the data to 
the warehouse , one has to write it to db while the other has to manage a special record.
-The two important roles in Redis Streams are Producer and Consumers.
-The Redis Stream data structure is maintained as an Append-Only Log. Once a data is appended into it,
it becomes immutable. It is indexed and order in terms of TimeStamp. It is basically like a Hash Set ds, where
there must at least one field. It is schema less

## Some commands about Redis Streams:
-XADD <stream_name> * key1 value1 key2 value2 ...
the * ensures the hash set is issued an unqiue id of the form of like:
5153135431565-0, where the first part is the timestamp in milisecond
and the second part is sequence number.
-XRANGE <stream_name> <timestamp1> <timestamp2> COUNT <limit>
-XREVRANGE <stream_name> <timestamp1> <timestamp2> COUNT <limit>
-XREVRANGE <stream_name> -+ COUNT <limit>
-XREAD STREAMS <stream_name> <id_greater_than>
-XREAD COUNT <limit> BLOCK <block_time> STREAMS <stream_name> <id_greater_than>

Redis follows a Triming Strategy to trim down the stream content to optimally.
-XTRIM <stream_name> MAXLEN <maximum_length_of_stream_allowed>
-XADD <stream_name> MAXLEN <maximum_length_of_stream_allowed> * key1 value1 key2 value2 ...
-XLEN <stream_name>

-----------------------------------------

## Some Great Reads on Redis Streams, Consumer Groups and Stream Consumer Group Pattern
[Redis Streams](https://medium.com/redis-with-raphael-de-lio/understanding-redis-streams-33aa96ca7206) | [Offcial Video for Redis Stream commands and operations](https://www.youtube.com/watch?v=Z8qcpXyMAiA)

[Redis Implementation in Python](https://medium.com/@abgkcode/exploring-redis-streams-real-time-data-processing-simplified-387827697460)

