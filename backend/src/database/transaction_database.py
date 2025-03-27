from src.database.db import connection
import time

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
        
    @staticmethod
    def get_lest_transactions_mes(idUser) -> list:
        """
        Retorna as últimas transações do usuário dos últimos 5 meses, agrupadas por mês.
        """       
        query = '''
            SELECT 
                TO_CHAR(data, 'Mon/YY') AS mes_ano,
                SUM(valor) AS total_valor,
                MAX(data) AS ultima_transacao
            FROM transactions 
            WHERE idUser = %s
            AND data >= NOW() - INTERVAL '5 months'
            GROUP BY mes_ano
            ORDER BY ultima_transacao;
        '''

        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
                
            print(resultado)
            resultado_final = {
                mes_ano: total_valor for mes_ano, total_valor, _ in resultado
            }
        
        return resultado_final
    
    @staticmethod
    def get_lest_transactions_mes_categoria(idUser) -> list:
        
        query = '''
            SELECT 
                categoria,
                SUM(valor) AS total_valor
            FROM transactions 
            WHERE idUser = %s
            AND data >= NOW() - INTERVAL '5 months'
            GROUP BY categoria
            ORDER BY total_valor DESC;
        '''

        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
            
            total_geral = sum(total_valor for _, total_valor in resultado)
            
            resultado_final = {
                categoria: {
                    "porcentagem": round((total_valor / total_geral) * 100, 2),
                    "total_gasto": total_valor,
                }
                for categoria, total_valor in resultado
            }

        return resultado_final