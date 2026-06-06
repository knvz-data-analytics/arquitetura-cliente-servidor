from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List

# FastAPI
app = FastAPI(title="API de Gerenciamento de Usuários")

# Pydantic pra validação
class Usuario(BaseModel):
    id: int
    nome: str
    email: str # Usando str

# Armazenamento em memória
usuarios_db: List[Usuario] = []

# Endpoint 1: (POST)
@app.post("/usuarios", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario):
    # Tratamento de erro: Verifica se o ID já existe
    for u in usuarios_db:
        if u.id == usuario.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Um usuário com este ID já existe no sistema."
            )
    
    # Tratamento de erro: Verifica se o email já existe
    for u in usuarios_db:
        if u.email == usuario.email:
             raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Um usuário com este email já está cadastrado."
            )
             
    # Adiciona na memória e retorna o usuário criado
    usuarios_db.append(usuario)
    return usuario

# Endpoint 2: (GET)
@app.get("/usuarios", response_model=List[Usuario], status_code=status.HTTP_200_OK)
def listar_usuarios():
    # Retorna a lista em memória
    return usuarios_db