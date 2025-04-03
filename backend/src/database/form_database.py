from src.database.db import connection

# Classe responsável pela interação com a tabela "perguntas" no banco de dados.
# Permite formatar, recuperar e inserir registros de formulários.
class FormDatabase:
    
    @staticmethod
    def format_form_data(form_tuple):
        """
        Formata os dados retornados do banco de dados para um dicionário.

        Parâmetros:
            form_tuple (tuple): Tupla contendo os dados de um formulário.

        Retorna:
            dict: Dicionário contendo os dados do formulário.
        """
        return {
            'resposta': form_tuple[0],
            'idUser': form_tuple[1]
        }
        
    @staticmethod
    def get_all_forms(idUser):
        """
        Recupera todas as respostas de formulários associadas a um usuário específico.

        Parâmetros:
            idUser (int): ID do usuário cujas respostas serão buscadas.

        Retorna:
            list: Lista de dicionários contendo os formulários do usuário.
        """
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
        """
        Insere uma nova resposta de formulário no banco de dados.

        Parâmetros:
            idUser (int): ID do usuário que está enviando a resposta.
            resposta (JSONB): Resposta do formulário em formato JSON.

        Retorna:
            bool: True se a inserção for bem-sucedida, False caso contrário.
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO perguntas (idUser, resposta) VALUES (%s, %s)", (idUser, resposta))
                conn.commit()
            conn.close()
            return True
        return False
