from datetime import datetime
from src.database.db import connection

class UserDatabase:
  
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
    def get_user_by_id(user_id):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE idUser = %s", (user_id,))
                user = cursor.fetchone()
            conn.close()
            return user
        return None

    @staticmethod
    def create_user(nome, sobrenome, email, senha):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (nome, sobrenome, email, senha, criado, atualizado) VALUES (%s, %s, %s, %s, %s, %s)",
                    (nome, sobrenome, email, senha, datetime.now(), datetime.now())
                )
                conn.commit()
            conn.close()

    @staticmethod
    def update_user(user_id, nome, sobrenome, email, senha):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE users SET nome = %s, sobrenome = %s, email = %s, senha = %s, atualizado = %s WHERE idUser = %s",
                    (nome, sobrenome, email, senha, datetime.now(), user_id)
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

