"""
Banco de dados - Aprender linguagens que te deixem modelar o banco
	- SQL (Linguagem de consulta Estruturada)
	- Caracteristicas:
		-SELECT * FROM (Nome da tabela) ; (ponto e virgula necessário para informar que acabou o comando.
		- Irá consultar o BD na tabela (senha da tabela)
		
		- SGDB:
			- Gerenciar permissões de acesso (quem pode fazer e o que pode fazer).
			- ADMINISTRADOR DE BANCO DE DADOS (DBA)
			- CRIAR CONSULTAS PERSONALIZADAS
			- SELECT * FROM CLIENTES;
	-ORM: MAPEAMENTO OBJETO RELACIONAL
        - USAR A LINGUAGEM DE PROGRAMAÇÃO PARA MANIPULAR O BANCO DE DADOS.
    - INSTALANDO ORM PARA PYTHON:
		-pip install sqlalchemy


"""

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados.
MEU_BANCO = create_engine("sqlite://meubanco.db")

#Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.

Base = declarative_base()
class Cliente(Base):
    __tablename__ = "clientes"
    
	#Definindo campos da tabela
    id = Column("id", Integer, primary_key= True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    
	def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        
base.metadata.create_all(bind = MEU_BANCO)