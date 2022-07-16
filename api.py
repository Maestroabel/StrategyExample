from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/myname")
async def root():
    return {"name": "Rosmery0"}

@app.get("/sumar")
async def root(numero1: int = 0, numero2: int = 0):
    return {"result": calc.sumar(numero1, numero2)}

@app.get("/restar")
async def root(numero1: int = 0, numero2: int = 0):
    return {"result": calc.restar(numero1, numero2)}


