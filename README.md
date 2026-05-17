# Simple REST API

A lightweight REST API built with Python and Flask for
managing tasks. Fully containerized with Docker.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/:id | Get a single task |
| POST | /tasks | Create a new task |
| PUT | /tasks/:id | Update a task |
| DELETE | /tasks/:id | Delete a task |

## Run with Docker

docker build -t simple-rest-api .
docker run -p 5000:5000 simple-rest-api

## Run with Python

pip install flask
python app.py

## Run Tests

python test_app.py

## Technologies
- Python 3.11
- Flask
- Docker
