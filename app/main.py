from fastapi import FastAPI

app = FastAPI()

#should print
@app.get("/")
def read_root():
    return {"Hello": "Fastapi in container, check before deploy the model"}
