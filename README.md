# Redis Stream Event Logger

A simple demo project to illustrate the use of **Redis Streams** and **consumer groups** with Python and FastAPI.  
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

