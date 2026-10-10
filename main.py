from fastapi import FastAPI, HTTPException
from fastapi import status
from pydantic import BaseModel
tasks = [{"id": 1, "title": "Learn FastAPI", "done": False}, 
         {"id": 2, "title": "Build a REST API", "done": False},         
         {"id": 3, "title": "Deploy the API", "done": False}    ]



class Task(BaseModel):
    id: int| None = None
    title: str 
    done: bool | None = None


app = FastAPI()



@app.get("/")
def hello():
    return {"name": "Task API", "version": "1.0.0","endpoints":["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id:int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
        if task.title == "":
            raise HTTPException(status_code=400, detail="Task title cannot be empty")
        else:
            task.id = max(t["id"] for t in tasks) + 1 
            task.done = False
           
            tasks.append((task.model_dump()))
   
        return task
