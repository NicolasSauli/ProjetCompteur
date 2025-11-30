# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser le front (sinon CORS error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en production, remplace "*" par ton domaine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Compteur stocké en mémoire
counter = {"value": 0}

@app.get("/get_counter")
def get_counter():
    """Renvoie la valeur actuelle du compteur"""
    return counter

@app.post("/increment")
def increment_counter():
    """Incrémente le compteur"""
    counter["value"] += 1
    return JSONResponse(content=counter)

@app.post("/decrement")
def decrement_counter():
    """Diminue le compteur"""
    counter["value"] -= 1
    return JSONResponse(content=counter)

