from fastapi import FastAPI, Query
from flask import Flask, request, jsonify
import json
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the specified CSV file
students = []
#return 'This is the first line of code'
file_path = 'q-vercel-python.json'
with open(file_path, 'r') as file:
          data_1=json.load(file)

#with open('q-vercel-python.json, mode='r') as file:
 #    reader = json.load(file)
    
  #  for row in reader:
   #     students.append({
    #        "name":  row["name"]),
     #       "marks": row["marks"]
      #  })

@app.get("/")
async def get_students(name_: Optional[List[str]] = Query(None)):
    print(f"Requested names: {name_}")  # Debugging line
    if name_:
        #filtered_students = [student for student in students if student["name"] in name_]
        filtered_data = [entry['marks'] for entry in data_1 if entry['name'] in name_] 
        print(f"Filtered students: {filtered_students}")  # Debugging line
        return {"marks": filtered_students}
    return {"marks": students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

#def read_root():
 #   file_path = 'q-vercel-python.json'  # JSON file path
  #  name_filter=request.args.getlist('name')
   # return 'reached here'
    #if not name_filter:
     #   return 'No names passed'
    #with open(file_path, 'r') as file:
     #   data_1=json.load(file)
    #filtered_data = [entry['marks'] for entry in data_1 if entry['name'] in name_filter] 
    #return {"marks": "Hello, World!"}
