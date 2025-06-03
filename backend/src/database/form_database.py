from src.database.db import connection
import json


# CREATE TABLE IF NOT EXISTS perguntas (
#   idUser INT NOT NULL,
#   resposta JSONB NOT NULL,
#   CONSTRAINT fk_pergunta_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
# );

class FormDatabase:
    
    @staticmethod
    def format_form_data(form_tuple):
        return {
            'resposta': form_tuple[1]
        }
        
    @staticmethod
    def get_all_forms(idUser):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM respostas WHERE idUser = %s", (idUser,))
                forms = cursor.fetchall()
            conn.close()
            print(forms)
            forms = [FormDatabase.format_form_data(form) for form in forms]
            return forms
        return []
    
    @staticmethod
    def create_form(idUser, resposta):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO respostas (idUser, resposta) VALUES (%s, %s)", (idUser, resposta))
                conn.commit()
            conn.close()
            return True
        return False
    
    @staticmethod
    def update_last_answer(idUser, new_resposta):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                # Busca as respostas atuais
                cursor.execute("SELECT resposta FROM respostas WHERE idUser = %s", (idUser,))
                result = cursor.fetchone()
                if result:
                    respostas = result[0] if isinstance(result[0], list) else json.loads(result[0])
                    if respostas:
                        # Altera a resposta da última pergunta
                        respostas[-1]['resposta'] = new_resposta
                        respostas_json = json.dumps(respostas)
                        cursor.execute("UPDATE respostas SET resposta = %s WHERE idUser = %s", (respostas_json, idUser))
                        conn.commit()
                        conn.close()
                        return True
            conn.close()
        return False