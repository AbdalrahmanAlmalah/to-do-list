# Task Management API

A simple RESTful CRUD API developed using **Python and FastAPI** as part of the **FlyRank Backend Development Internship — Week 2 Assignment**.

The application allows users to create, retrieve, update, delete, filter, and search tasks. It also includes task statistics, reset functionality, and interactive API documentation through Swagger UI.

## Features

### Core Features

- Create a task with an automatically generated ID.
- Retrieve all tasks.
- Retrieve a specific task by ID.
- Update a task's title or completion status.
- Delete a task.
- Validate task input.
- Handle HTTP errors.
- Check API health.
- Test endpoints using Swagger UI.

### Optional Extras

- **Filtering:** Filter tasks by completion status.
- **Search:** Search for tasks by title.
- **Statistics:** Retrieve the total and completed task counts.
- **Reset:** Restore the three original example tasks.
- **In-Memory Experiment:** Observe how restarting the server resets stored data.

## Technologies Used

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- Swagger UI / OpenAPI
- Git and GitHub

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AbdalrahmanAlmalah/to-do-list.git
cd to-do-list
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (CMD):**

```bat
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Server

```bash
uvicorn main:app --reload --port 8080
```

The API is available at:

http://localhost:8080

Interactive documentation:

http://localhost:8080/docs

## API Endpoints

### Core Endpoints

| Method | Endpoint | Description | Success Status |
|---|---|---|---|
| GET | `/` | Returns API information | 200 |
| GET | `/health` | Checks API health | 200 |
| GET | `/tasks` | Retrieves all tasks | 200 |
| GET | `/tasks/{id}` | Retrieves a task by ID | 200 |
| POST | `/tasks` | Creates a new task | 201 |
| PUT | `/tasks/{id}` | Updates an existing task | 200 |
| DELETE | `/tasks/{id}` | Deletes a task | 204 |

### Optional Endpoints and Query Parameters

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks?done=true` | Returns completed tasks |
| GET | `/tasks?done=false` | Returns incomplete tasks |
| GET | `/tasks?search=API` | Searches tasks by title |
| GET | `/tasks?stats=true` | Returns task statistics |
| POST | `/reset` | Restores the original three tasks |

**Note:** Filtering, search, and statistics currently use the same GET endpoint. If multiple parameters are provided, the API handles them according to the current conditional order: `done`, then `stats`, then `search`.

## Example API Requests

### 1. Get All Tasks

```bash
curl -i http://localhost:8080/tasks
```

### 2. Get a Specific Task

```bash
curl -i http://localhost:8080/tasks/1
```

### 3. Create a New Task

```bash
curl -i -X POST http://localhost:8080/tasks -H "Content-Type: application/json" -d "{\"title\":\"Learn Docker\"}"
```

Example response:

```json
{
  "id": 4,
  "title": "Learn Docker",
  "done": false
}
```

HTTP Status: `201 Created`

### 4. Update a Task

```bash
curl -i -X PUT http://localhost:8080/tasks/4 -H "Content-Type: application/json" -d "{\"done\":true}"
```

Example response:

```json
{
  "id": 4,
  "title": "Learn Docker",
  "done": true
}
```

### 5. Delete a Task

```bash
curl -i -X DELETE http://localhost:8080/tasks/4
```

HTTP Status: `204 No Content`

### 6. Filter Tasks

Completed tasks:

```bash
curl -i "http://localhost:8080/tasks?done=true"
```

Incomplete tasks:

```bash
curl -i "http://localhost:8080/tasks?done=false"
```

### 7. Search Tasks

```bash
curl -i "http://localhost:8080/tasks?search=API"
```

Search is case-insensitive and matches text within task titles.

### 8. Task Statistics

```bash
curl -i "http://localhost:8080/tasks?stats=true"
```

Example response for the original three tasks:

```json
{
  "total_tasks": 3,
  "completed_tasks": 0
}
```

### 9. Reset Tasks

```bash
curl -i -X POST http://localhost:8080/reset
```

The reset operation removes existing tasks and restores the original three sample tasks with their initial IDs and completion statuses.

## Actual cURL Test Result

The following output was captured while testing the API locally on October 10, 2026.

**Command:**

```bash
curl -i http://localhost:8080/tasks
```

**Actual Response:**

```http
HTTP/1.1 200 OK
date: Sat, 10 Oct 2026 11:47:27 GMT
server: uvicorn
content-length: 143
content-type: application/json

[{"id":1,"title":"Learn FastAPI","done":false},{"id":2,"title":"Build a REST API","done":false},{"id":3,"title":"Deploy the API","done":false}]
```

The request returned HTTP `200 OK` with the tasks stored in memory.

## Swagger UI Documentation

FastAPI automatically generates interactive documentation using OpenAPI.

Visit:

http://localhost:8080/docs

Swagger UI supports testing the API directly from the browser through the **Try it out** feature.

### Swagger Screenshot

![Swagger UI Screenshot](swagger.png)

## Data Storage

The application uses an in-memory Python list instead of a database.

The initial data contains three example tasks.

Newly created tasks and updates are stored only while the server process remains active.

### In-Memory Persistence Experiment

To test this behavior:

1. Start the API server.
2. Create a new task using POST `/tasks`.
3. Verify that the task exists using GET `/tasks`.
4. Stop the server.
5. Start the server again.
6. Retrieve all tasks.

**Observation:** Tasks created during runtime disappear after restarting the server, and the original three tasks are restored. This happens because the application stores data in Python memory rather than persistent database storage.

## Known Limitations

- No database or persistent storage.
- No authentication or authorization.
- No automated test suite.
- Statistics use a query parameter rather than a dedicated endpoint.
- Combined search and completion-status filtering is not currently supported.

## Future Improvements

- Integrate PostgreSQL or SQLite.
- Add user authentication.
- Implement pagination.
- Support combining search and filtering.
- Introduce a dedicated `/stats` endpoint.
- Add automated tests with Pytest.
- Deploy the application to a cloud hosting service.

## Author

**Abdalrahman Almalah**

GitHub: https://github.com/AbdalrahmanAlmalah

**Project:** FlyRank Backend Development Internship — Week 2

**Assignment:** Build Your First CRUD API