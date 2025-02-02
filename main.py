from fastapi import FastAPI
from flask import request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    file_path = 'q-vercel-python.json'  # JSON file path
    name_filter=request.args.getlist('name')
    return name_filter
    #if not name_filter:
     #   return 'No names passed'
    #with open(file_path, 'r') as file:
     #   data_1=json.load(file)
    #filtered_data = [entry['marks'] for entry in data_1 if entry['name'] in name_filter] 
    #return {"marks": "Hello, World!"}
