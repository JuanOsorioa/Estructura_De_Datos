'''# Para correr el servidor: uvicorn server:app --reload
# se debe instalar uvicorn: pip install uvicorn
# se debe instalar FastAPI: pip install fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from paquete.cola import Cola

app = FastAPI()
cola = Cola()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/estado")
def estado():
    elementos = cola.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar")
def encolar(item: dict):
    cola.encolar(item)
    return {"status": "ok"}

@app.get("/desencolar")
def desencolar():
    elemento = cola.desencolar()
    return {"status": "ok", "elemento": elemento}

@app.get("/ver_primero")
def ver_primero():
    elementos = cola.ver_primero()
    return {"status": "ok", "elementos": elementos}

@app.get("/ver_listado")
def ver_listado():
    elementos = cola.ver_listado()
    return {"status": "ok", "elementos": elementos}

@app.get("/ver_ultimo")
def ver_ultimo():
    elementos = cola.ver_ultimo()
    return {"status": "ok", "elementos": elementos}
'''
