# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from scraper import buscar_productos
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lista de orígenes permitidos (puede ser '*', pero no es recomendable en producción)
origins = [
    "http://localhost:4200",  # frontend Angular local
]

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # O ['*'] para permitir todo
    allow_credentials=True,
    allow_methods=["*"],                # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],                # Permitir todos los headers
)

class Consulta(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI"}

@app.post("/api/products")
def buscar(consulta: Consulta):
    resultados = buscar_productos(consulta.query)
    return {"products": resultados}