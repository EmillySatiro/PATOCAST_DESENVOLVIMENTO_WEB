from datetime import datetime
from src.database.db import connection
from decimal import Decimal
import random
class UserDatabase:

    @staticmethod
    def format_user_data(user_tuple):
        return {
            "idUser": user_tuple[0],
            "nome": user_tuple[1],
            "sobrenome": user_tuple[2],
            "email": user_tuple[3],
            "senha": user_tuple[4],
            "limite": float(user_tuple[5]) if isinstance(user_tuple[5], Decimal) else user_tuple[5],
            "criado": user_tuple[6].strftime("%Y-%m-%d %H:%M:%S.%f") if isinstance(user_tuple[6], datetime) else user_tuple[6],
            "atualizado": user_tuple[7].strftime("%Y-%m-%d %H:%M:%S.%f") if isinstance(user_tuple[7], datetime) else user_tuple[7]
        }
        
    @staticmethod
    def get_new_password(user_id) -> str:
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                new_password = random.randrange(0, 100000)
                new_password = str(new_password)
                new_password = new_password.zfill(6)
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
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    '''
                        INSERT INTO 
                        users (nome, sobrenome, email, senha, limite ,criado, atualizado) 
                        VALUES (%s, %s, %s, crypt(%s,gen_salt('bf')), %s, %s, %s) returning idUser;
                    ''',
                    (nome, sobrenome, email, senha, random.randrange(1000, 10000), datetime.now(), datetime.now())
                )
                conn.commit()
                user_id = cursor.fetchone()[0]
            conn.close()
            return user_id
        
        return False

    @staticmethod
    def update_user(user_id, **kwargs):
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
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE idUser = %s", (user_id,))
                conn.commit()
            conn.close()
    
    @staticmethod
    def connect_user(email,senha) -> tuple:
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                        SELECT * FROM users 
                        WHERE email = %s AND senha = crypt(%s, senha);
                    ''', 
                    (email,senha)
                )
                user = cursor.fetchone()
            conn.close()
            if user:
                return (True, UserDatabase.format_user_data(user))
        return False, None

