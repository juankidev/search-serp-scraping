# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from scraper import buscar_productos

app = FastAPI()

class Consulta(BaseModel):
    query: str

@app.post("/buscar")
def buscar(consulta: Consulta):
    resultados = buscar_productos(consulta.query)
    return {"productos": resultados}