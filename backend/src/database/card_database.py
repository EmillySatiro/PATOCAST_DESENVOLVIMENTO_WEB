from src.database.db import connection

class CardDatabase:
  
  @staticmethod
  def format_card_data(card_tuple):
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
    conn = connection()
    print(idUser)
    if conn:
      with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM cartao WHERE idUser = %s", (idUser,))
        cards = cursor.fetchall()
      conn.close()
      cards = [CardDatabase.format_card_data(card) for card in cards]
      return cards
    return []

  @staticmethod
  def create_card(idUser, numero, nome, meta,tipo):
    conn = connection()
    if conn:
      with conn.cursor() as cursor:
        cursor.execute(
          "INSERT INTO cartao (idUser, numero, nome, meta, tipo) VALUES (%s, %s, %s, %s, %s)",
          (idUser, numero, nome, meta, tipo)
        )
        conn.commit()
      conn.close()
