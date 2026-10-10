from fastapi import FastAPI, HTTPException
from fastapi import status
from pydantic import BaseModel
tasks = [{"id": 1, "title": "Learn FastAPI", "done": False}, 
         {"id": 2, "title": "Build a REST API", "done": False},         
         {"id": 3, "title": "Deploy the API", "done": False}    ]



class Task(BaseModel):
    id: int| None = None
    title: str   | None = None
    done: bool | None = None


app = FastAPI(
    title="Task API",
    description="An API for managing tasks. This API allows you to create, read, update, and delete tasks.",
    summary="Task API summary",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)



@app.get("/", description="Returns a welcome message and API information.")
def hello():
    return {"name": "Task API", "version": "0.0.1","endpoints":["/tasks"]}

@app.get("/health",description="Returns the health status of the API.")
def health():
    return {"status": "ok"}


@app.get("/tasks", description="Returns tasks with optional filtering, search, and statistics.")
def get_tasks(
    done: bool | None = None,
    stats: bool | None = None,
    search: str | None = None
):
    if done is not None:
        filtered_tasks = [task for task in tasks if task["done"] == done]
        return filtered_tasks

    if stats is not None:
        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task["done"]])
        pending_tasks = total_tasks - completed_tasks

        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks
        }

    if search is not None:
        tasks_search = [
            task for task in tasks
            if search.lower() in task["title"].lower()
        ]
        return tasks_search

    return tasks

@app.get("/tasks/{id}",description="Returns a specific task by ID.")
def get_task(id:int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED,description="Creates a new task.")
def create_task(task: Task):
        if task.title == "" or task.title is None or task.title == " ":
            raise HTTPException(status_code=400, detail="Task title cannot be empty")
        else:
            task.id = max(t["id"] for t in tasks) + 1 
            task.done = False
           
            tasks.append((task.model_dump()))
   
        return task

@app.put("/tasks/{id}", description="Updates a specific task by ID.")
def update_task(id: int, task: Task):
    for t in tasks:
        if t["id"] == id:

            if task.title is not None:
                if not task.title.strip():
                    raise HTTPException(
                        status_code=400,
                        detail="Task title cannot be empty"
                    )
                t["title"] = task.title

            if task.done is not None:
                t["done"] = task.done

            return t

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT, description="Deletes a specific task by ID.")
def delete_task(id: int):
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return None

    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/reset", description="Resets all tasks to the original three example tasks.")
def reset_tasks():
    tasks.clear()

    tasks.extend([
        {"id": 1, "title": "Learn FastAPI", "done": False},
        {"id": 2, "title": "Build a REST API", "done": False},
        {"id": 3, "title": "Deploy the API", "done": False}
    ])

    return {
        "message": "Tasks have been reset successfully.",
        "tasks": tasks
    }