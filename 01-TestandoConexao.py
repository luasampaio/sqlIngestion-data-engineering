import pyodbc

# Configuração da conexão
server = "SAMPAIO"   # Nome do servidor SQL ou IP
database = "DESENVOLVIMENTO"    # Nome do banco de dados

# Criando a conexão com Windows Authentication
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};"
    "Trusted_Connection=yes;"
)

# Criando um cursor
cursor = conn.cursor()

# Testando a conexão com uma consulta simples
cursor.execute("SELECT * FROM [FILMES].[dbo].[FILME]")
for row in cursor.fetchall():
    print(row)

# Fechando conexão
cursor.close()

conn.close()
