from fastapi import FastAPI

app = FastAPI()

@app.get("")
def login(id:int,):
    

