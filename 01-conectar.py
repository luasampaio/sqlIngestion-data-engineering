import pyodbc
import pandas as pd

# Configuração da conexão
server = "SAMPAIO"   # Nome do servidor SQL ou IP
database = "DESENVOLVIMENTO"    # Nome do banco de dados

# Criando a conexão com Windows Authentication
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};"
    "Trusted_Connection=yes;"
)

# Criando DataFrame a partir da consulta SQL
query = "SELECT * FROM [FILMES].[dbo].[FILME]"

df = pd.read_sql(query, conn)

# Exibir os 5 primeiros registros
print(df.head())

# Fechando a conexão
conn.close()
