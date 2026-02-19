from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal

app = FastAPI()

#Cria as tabelas no banco 
models.Base.metadata.create_all(bind=engine)

#Função para abrir e fechar conexão com o banco
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "API com banco SQLite funcionando!"}

#Rota post real (salva no banco)
@app.post("/clientes")
def criar_cliente(nome: str, email: str, db: Session = Depends(get_db)):
    novo_cliente = models.Cliente(nome=nome, email=email)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return {"mensagem": "Cliente salvo no banco", "id": novo_cliente.id}

#Criar get de clientes
@app.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all() #pega todos os registros da tabela clientes e devolve como lista
    return clientes

#Buscar cliente por ID
@app.get("/clientes/{cliente_id}")
def buscar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if cliente:
        return cliente
    return {"erro": "Cliente não encontrado"}

#Update de dados 
@app.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, nome: str, email: str, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not cliente: 
        return {"erro": "Cliente não encontrado"}
    cliente.nome = nome
    cliente.email = email 

    db.commit()
    db.refresh(cliente)

    return {"mensagem": "Cliente atualizado com sucesso"}
#Delete//apaga dados do banco
@app.delete("/cliente/{cliente_id}")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not cliente: 
        return {"erro": "Cliente não encontrado"}
    
    db.delete(cliente)
    db.commit()

    return{"mensagem": "Cliente deletado com sucesso"}

