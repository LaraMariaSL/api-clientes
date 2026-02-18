from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

# Caminho do banco SQLite 
DATABASE_URL = "sqlite:///./clientes.db"


# Cria conexão com o banco 
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sessão para conversar com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para criação das tabelas
Base = declarative_base()