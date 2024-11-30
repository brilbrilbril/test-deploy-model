from fastapi import FastAPI

app = FastAPI()

#should print
@app.get("/")
def read_root():
    return {"Hello": "Fastapi in container, check before deploy the model"}

@app.get("/task")
def perform_task():
    return {"Task": "This is another task executed via a different route"}