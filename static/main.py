from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


counter = {"value": 0}

@app.get("/get_counter")
def get_counter():
    return counter

@app.post("/increment")
def increment_counter():
    counter["value"] += 1
    return JSONResponse(content=counter)

@app.post("/decrement")
def decrement_counter():
    counter["value"] -= 1
    return JSONResponse(content=counter)

