from src.database.db import connection

class CardDatabase:
    """
    Classe responsável por gerenciar as operações no banco de dados relacionadas aos cartões.
    """
  
    @staticmethod
    def format_card_data(card_tuple):
        """
        Formata os dados do cartão obtidos do banco de dados em um dicionário.
        
        :parametro card_tuple: Tupla com os dados do cartão.
        :return: Dicionário contendo as informações do cartão.
        """
        return {
            "idCartao": card_tuple[0],
            "idUser": card_tuple[1],
            "numero": card_tuple[2],
            "nome": card_tuple[3],
            "meta": float(card_tuple[4]),
            "tipo": card_tuple[5]
        }
  
    @staticmethod
    def get_all_cards(idUser):
        """
        Recupera todos os cartões de um usuário específico.
        
        :parametro idUser: ID do usuário.
        :return: Lista de dicionários contendo os cartões do usuário.
        """
        conn = connection()
        print(idUser)  # Debug: Exibe o ID do usuário no console
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM cartao WHERE idUser = %s", (idUser,))
                cards = cursor.fetchall()
            conn.close()
            cards = [CardDatabase.format_card_data(card) for card in cards]
            return cards
        return []

    @staticmethod
    def create_card(idUser, numero, nome, meta, tipo):
        """
        Cria um novo cartão para o usuário.
        
        :parametro idUser: ID do usuário.
        :parametro numero: Número do cartão.
        :parametro nome: Nome associado ao cartão.
        :parametro meta: Meta financeira associada ao cartão.
        :parametro tipo: Tipo do cartão (ex: crédito ou débito).
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO cartao (idUser, numero, nome, meta, tipo) VALUES (%s, %s, %s, %s, %s)",
                    (idUser, numero, nome, meta, tipo)
                )
                conn.commit()
            conn.close()

    @staticmethod
    def update_card(idCartao, **kwargs):
        """
        Atualiza um cartão existente com os novos valores informados.
        
        :parametro idCartao: ID do cartão a ser atualizado.
        :parametro kwargs: Parâmetros a serem atualizados (ex: nome, meta, tipo, etc.).
        """
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                for key, value in kwargs.items():
                    cursor.execute(f"UPDATE cartao SET {key} = %s WHERE idCartao = %s", (value, idCartao))
                conn.commit()
            conn.close()