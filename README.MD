# API de Cadastro de Clientes

Este projeto é uma API REST desenvolvida com **FastAPI**, utilizando **SQLAlchemy** e **SQLite** para persistência de dados.

## Funcionalidades

* Criar clientes
* Listar clientes
* Buscar cliente por ID
* Atualizar cliente
* Deletar cliente

## Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite

## Como executar o projeto

1. Criar ambiente virtual:

```
python -m venv venv
```

2. Ativar o ambiente:

```
venv\Scripts\activate
```

3. Instalar dependências:

```
pip install -r requirements.txt
```

4. Rodar o servidor:

```
uvicorn main:app --reload
```

Acesse no navegador:

```
http://127.0.0.1:8000/docs
```
