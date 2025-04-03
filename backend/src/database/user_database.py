from datetime import datetime
from src.database.db import connection
from decimal import Decimal
import random

class UserDatabase:
    """
    Classe para manipulação de dados dos usuários no banco de dados.
    """

    @staticmethod
    def format_user_data(user_tuple):
        """
        Formata os dados do usuário em um dicionário.
        
        :param user_tuple: Tupla contendo os dados do usuário.
        :return: Dicionário com os dados formatados.
        """
        return {
            "idUser": user_tuple[0],
            "nome": user_tuple[1],
            "sobrenome": user_tuple[2],
            "email": user_tuple[3],
            "senha": user_tuple[4],
            "criado": user_tuple[5].strftime("%Y-%m-%d %H:%M:%S.%f") if isinstance(user_tuple[5], datetime) else user_tuple[5],
            "atualizado": user_tuple[6].strftime("%Y-%m-%d %H:%M:%S.%f") if isinstance(user_tuple[6], datetime) else user_tuple[6]
        }
    
    @staticmethod
    def get_new_password(user_id) -> str:
        """
        Gera uma nova senha para o usuário e a atualiza no banco de dados.
        
        :param user_id: ID do usuário.
        :return: Nova senha gerada.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                new_password = str(random.randrange(0, 100000)).zfill(6)
                cursor.execute(
                    '''
                        UPDATE users 
                        SET senha = crypt(%s, gen_salt('bf')), atualizado = %s 
                        WHERE idUser = %s
                    ''',
                    (new_password, datetime.now(), user_id)
                )
                conn.commit()
            conn.close()
            return new_password
        return None
    
    @staticmethod
    def get_user_by_email(email):
        """
        Busca um usuário pelo email.
        
        :param email: Email do usuário.
        :return: Dicionário com os dados do usuário ou None se não encontrado.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()
            conn.close()
            return UserDatabase.format_user_data(user) if user else None
        return None
    
    @staticmethod
    def get_all_users():
        """
        Retorna todos os usuários cadastrados.
        
        :return: Lista de usuários.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
            conn.close()
            return users
        return []

    @staticmethod
    def update_user_password(email, password):
        """
        Atualiza a senha de um usuário pelo email.
        
        :param email: Email do usuário.
        :param password: Nova senha.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    '''
                        UPDATE users 
                        SET senha = crypt(%s, gen_salt('bf')), atualizado = %s 
                        WHERE email = %s
                    ''',
                    (password, datetime.now(), email)
                )
                conn.commit()
            conn.close()
    
    @staticmethod
    def get_user_by_id(user_id):
        """
        Busca um usuário pelo ID.
        
        :param user_id: ID do usuário.
        :return: Dicionário com os dados do usuário ou None se não encontrado.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE idUser = %s", (user_id,))
                user = cursor.fetchone()
            conn.close()
            return UserDatabase.format_user_data(user)
        return None

    @staticmethod
    def create_user(nome, sobrenome, email, senha):
        """
        Cria um novo usuário no banco de dados.
        
        :param nome: Nome do usuário.
        :param sobrenome: Sobrenome do usuário.
        :param email: Email do usuário.
        :param senha: Senha do usuário.
        :return: ID do usuário criado ou False em caso de falha.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    '''
                        INSERT INTO 
                        users (nome, sobrenome, email, senha, criado, atualizado) 
                        VALUES (%s, %s, %s, crypt(%s,gen_salt('bf')), %s, %s) returning idUser;
                    ''',
                    (nome, sobrenome, email, senha, datetime.now(), datetime.now())
                )
                conn.commit()
                user_id = cursor.fetchone()[0]
            conn.close()
            return user_id
        
        return False

    @staticmethod
    def update_user(user_id, **kwargs):
        """
        Atualiza os dados de um usuário.
        
        :param user_id: ID do usuário.
        :param kwargs: Campos a serem atualizados.
        """
        if not kwargs or not (conn := connection()):
            return

        with conn.cursor() as cursor:
            campos = ", ".join(
                "senha = crypt(%s, gen_salt('bf'))" if k == "senha" else f"{k} = %s"
                for k in kwargs
            )
            valores = [v for v in kwargs.values()]
            valores.extend([datetime.now(), user_id])
            
            cursor.execute(
                f"UPDATE users SET {campos}, atualizado = %s WHERE idUser = %s",
                valores
            )
            conn.commit()
        conn.close()
    
    @staticmethod
    def delete_user(user_id):
        """
        Remove um usuário do banco de dados.
        
        :param user_id: ID do usuário.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE idUser = %s", (user_id,))
                conn.commit()
            conn.close()
    
    @staticmethod
    def connect_user(email, senha) -> tuple:
        """
        Verifica se o usuário existe e se a senha está correta.
        
        :param email: Email do usuário.
        :param senha: Senha do usuário.
        :return: Tupla (True, dados do usuário) se autenticado, caso contrário (False, None).
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    '''
                        SELECT * FROM users 
                        WHERE email = %s AND senha = crypt(%s, senha);
                    ''',
                    (email, senha)
                )
                user = cursor.fetchone()
            conn.close()
            return (True, UserDatabase.format_user_data(user)) if user else (False, None)
