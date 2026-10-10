from fastapi import FastAPI, HTTPException
from fastapi import status
tasks = [{"id": 1, "title": "Learn FastAPI", "done": False}, 
         {"id": 2, "title": "Build a REST API", "done": False},         
         {"id": 3, "title": "Deploy the API", "done": False}    ]


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

@app.get("/tasks/{id}", status_code=status.HTTP_200_OK)
def get_task(id:int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")