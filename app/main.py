from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# define text generation model
generator = pipeline('text-generation', model='gpt2')

# define a Pydantic model for the request body
class GenerateRequest(BaseModel):
    processed_data: str

# simple text generation model
@app.post("/generate")
def generate_text(request: GenerateRequest):
    result = generator(request.processed_data, max_length=50, num_return_sequences=1)
    return {"generated_text": result[0]['generated_text']}

# it's like welcoming page
@app.get("/")
def read_root():
    return {"Hello": "Fastapi inside GKE"}

# test different route
@app.get("/task")
def perform_task():
    return {"Task": "This is another task executed via a different route"}