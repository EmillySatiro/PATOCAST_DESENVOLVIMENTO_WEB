from src.database.db import connection

class TransactionDatabase:

    @staticmethod
    def format_transaction(transaction_tuple):
        print(type(transaction_tuple[4]))
        return {
            "idTransaction": transaction_tuple[0],
            "idUser": transaction_tuple[1],
            "estabelecimento": transaction_tuple[2],
            "categoria": transaction_tuple[3],
            "valor": float(transaction_tuple[4]),
            "data": transaction_tuple[5].strftime("%d/%m/%Y")
        }
    
    @staticmethod
    def get_all_transactions(idUser) -> tuple:
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                        SELECT * FROM transactions 
                        WHERE idUser = (SELECT idUser FROM users WHERE idUser = %s)
                        ORDER BY data DESC;
                    ''', 
                    (idUser,)
                )
                transactions = cursor.fetchall()
            conn.close()
            return transactions