import psycopg2
from os import getenv

def connection():
    """
    Estabelece uma conexão com o banco de dados PostgreSQL utilizando variáveis de ambiente.

    Retorna:
        psycopg2.extensions.connection: Objeto de conexão com o banco de dados, se bem-sucedido.
        None: Se ocorrer um erro na conexão.

    Exceções:
        Captura exceções gerais e imprime a mensagem de erro caso a conexão falhe.
    """
    try:
        conn = psycopg2.connect(
            dbname=getenv("POSTGRES_DB"),      # Nome do banco de dados
            user=getenv("POSTGRES_USER"),      # Usuário do banco de dados
            password=getenv("POSTGRES_PASSWORD"),  # Senha do banco de dados
            host=getenv("POSTGRES_HOST"),      # Host do banco de dados
            port=getenv("POSTGRES_PORT"),      # Porta do banco de dados
        )
        print("Connected to the database")  # Mensagem de sucesso na conexão
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")  # Exibe erro em caso de falha
        return None