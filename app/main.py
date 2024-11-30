from fastapi import FastAPI
import os
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline('text-generation', model='gpt2')

# Define a Pydantic model for the request body
class GenerateRequest(BaseModel):
    processed_data: str

@app.post("/generate")
def generate_text(request: GenerateRequest):
    result = generator(request.processed_data, max_length=50, num_return_sequences=1)
    return {"generated_text": result[0]['generated_text']}

#should print
@app.get("/")
def read_root():
    return {"Hello": "Fastapi in container, check before deploy the model"}

@app.get("/task")
def perform_task():
    return {"Task": "This is another task executed via a different route"}