from src.database.db import connection


# CREATE TABLE IF NOT EXISTS perguntas (
#   idUser INT NOT NULL,
#   resposta JSONB NOT NULL,
#   CONSTRAINT fk_pergunta_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
# );

class FormDatabase:
    
    @staticmethod
    def format_form_data(form_tuple):
        return {
            'resposta': form_tuple[0]
        }
        
    @staticmethod
    def get_all_forms(idUser):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM perguntas WHERE idUser = %s", (idUser,))
                forms = cursor.fetchall()
            conn.close()
            forms = [FormDatabase.format_form_data(form) for form in forms]
            return forms
        return []
    
    @staticmethod
    def create_form(idUser, resposta):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO perguntas (idUser, resposta) VALUES (%s, %s)", (idUser, resposta))
                conn.commit()
            conn.close()
            return True
        return False