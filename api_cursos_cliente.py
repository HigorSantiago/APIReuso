# API com FastAPI
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from typing import List

app = FastAPI()

# Modelo do Curso
class Curso(BaseModel):
    id: int
    titulo: str
    descricao: str
    carga_horaria: int

# Banco de dados em memória
cursos = {}

# Listar todos os cursos
@app.get("/cursos", response_model=List[Curso])
def listar_cursos():
    return list(cursos.values())

# Obter detalhes de um curso específico
@app.get("/cursos/{id}", response_model=Curso)
def obter_curso(id: int):
    if id not in cursos:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return cursos[id]

# Criar um novo curso
@app.post("/cursos", response_model=Curso)
def criar_curso(curso: Curso):
    if curso.id in cursos:
        raise HTTPException(status_code=400, detail="ID do curso já existe")
    cursos[curso.id] = curso
    return curso

# Atualizar um curso existente
@app.put("/cursos/{id}", response_model=Curso)
def atualizar_curso(id: int, curso: Curso):
    if id not in cursos:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    cursos[id] = curso
    return curso

# Excluir um curso
@app.delete("/cursos/{id}", response_model=dict)
def excluir_curso(id: int):
    if id not in cursos:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    del cursos[id]
    return {"message": "Curso excluído com sucesso"}

# Cliente em Python
import requests

BASE_URL = "http://127.0.0.1:8000/cursos"

def listar_cursos():
    response = requests.get(BASE_URL)
    print(response.json())

def obter_curso(id):
    response = requests.get(f"{BASE_URL}/{id}")
    print(response.json())

def criar_curso(curso):
    response = requests.post(BASE_URL, json=curso)
    print(response.json())

def atualizar_curso(id, curso):
    response = requests.put(f"{BASE_URL}/{id}", json=curso)
    print(response.json())

def excluir_curso(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    print(response.json())

# Exemplos de uso do cliente
if __name__ == "__main__":
    # Criar um curso
    novo_curso = {"id": 1, "titulo": "Python para Iniciantes", "descricao": "Curso introdutório de Python", "carga_horaria": 40}
    criar_curso(novo_curso)

    # Listar cursos
    listar_cursos()

    # Obter detalhes do curso
    obter_curso(1)

    # Atualizar curso
    curso_atualizado = {"id": 1, "titulo": "Python Avançado", "descricao": "Curso avançado de Python", "carga_horaria": 60}
    atualizar_curso(1, curso_atualizado)

    # Excluir curso
    excluir_curso(1)
