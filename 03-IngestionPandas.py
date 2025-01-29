import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# Configuração do servidor e banco de dados
server = "SAMPAIO"
database = "DESENVOLVIMENTO"

# Criando a engine de conexão com Windows Authentication
engine = create_engine(
    f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server".replace(" ", "+")
)

# Definir a consulta SQL
query = "SELECT * FROM [FILMES].[dbo].[FILME]"

# Carregar os dados diretamente para um DataFrame Pandas
df = pd.read_sql(query, engine)

# Exibir os primeiros registros
print(df.head())
