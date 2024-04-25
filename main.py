from fastapi import FastAPI

app = FastAPI()
@app.get("/Welcome")
def root():
    print("Estoy dentro de la app")
    return{
        "message" : "Hellow World"
    }

