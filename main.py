from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    file_path = 'q-vercel-python.json'  # JSON file path
    #name_filter=request.args.getlist('name')
    return file_path
    #if not name_filter:
     #   return 'No names passed'
    #with open(file_path, 'r') as file:
     #   data_1=json.load(file)
    #filtered_data = [entry['marks'] for entry in data_1 if entry['name'] in name_filter] 
    #return {"marks": "Hello, World!"}
