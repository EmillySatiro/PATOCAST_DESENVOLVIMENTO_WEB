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
        
    @staticmethod
    def get_lest_transactions_mes(idUser) -> dict:
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
            GROUP BY mes_ano;
        '''

        resultado_final = {}
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
                resultado = sorted(resultado, key=lambda x: x[2], reverse=False)
                resultado_final = {
                    mes_ano: float(total_valor) for mes_ano, total_valor, _ in resultado
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
            AND data <= NOW() - INTERVAL '1 months'
            GROUP BY categoria
            ORDER BY categoria ASC;
        '''

        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
            
            total_geral = sum(total_valor for _, total_valor in resultado)
            
            resultado_final = {
                categoria: {
                    "porcentagem": float(round((total_valor / total_geral) * 100, 2)),
                    "total_gasto": float(total_valor),
                }
                for categoria, total_valor in resultado
            }

        return resultado_final
    
    @staticmethod
    def get_transactions_predict_next_mes(IdUser) -> list:
        """
        Retorna as transações previstas para o próximo mês.
        """       
        query = '''
            SELECT 
                TO_CHAR(data, 'Mon/YY') AS mes_ano,
                SUM(valor) AS total_valor,
                MAX(data) AS ultima_transacao
            FROM transactions 
            WHERE idUser = %s
            AND data >= NOW()
            AND data < NOW() + INTERVAL '1 months'
            GROUP BY mes_ano;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (IdUser,))
                resultado = cursor.fetchall()
                
            resultado_final = {
                'pendente': float(total_valor) for mes_ano, total_valor, _ in resultado
            }
            
        return resultado_final
    
    @staticmethod
    def get_transactions_days_in_current_week(IdUser) -> list:
        """
        Retorna as transações dos últimos 7 dias.
        """       
        query = '''
            SELECT 
                TO_CHAR(data, 'DD/Mon') AS dia,
                SUM(valor) AS total_valor
            FROM transactions 
            WHERE idUser = %s
            AND data <= NOW()
            AND data > NOW() - INTERVAL '1 months'
            GROUP BY dia;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (IdUser,))
                resultado = cursor.fetchall()
                
            resultado_final = {
                dia: float(total_valor) for dia, total_valor in resultado
            }
            
        return resultado_final