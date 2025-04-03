from src.database.db import connection

class TransactionDatabase:
    """
    Classe para interagir com o banco de dados e gerenciar transações financeiras do usuário.
    """
    
    @staticmethod
    def format_transaction(transaction_tuple):
        """
        Formata os dados de uma transação em um dicionário.
        """
        return {
            "idTransaction": transaction_tuple[0],
            "idUser": transaction_tuple[1],
            "estabelecimento": transaction_tuple[2],
            "categoria": transaction_tuple[3],
            "valor": float(transaction_tuple[4]),
            "data": transaction_tuple[5].strftime("%d/%m/%Y")
        }
    
    @staticmethod
    def get_all_transactions(idUser, mes=None, categoria=None) -> list:
        """
        Retorna todas as transações de um usuário, com filtros opcionais de mês e categoria.
        """
        conn = connection()
        if conn:
            query = '''
                SELECT * FROM transactions 
                WHERE idUser = %s
            '''
            params = [idUser]

            if mes and mes != 'todos':
                query += " AND TO_CHAR(data, 'YYYY-MM') = %s"
                params.append(mes)

            if categoria and categoria != 'todas':
                query += " AND categoria = %s"
                params.append(categoria)

            query += " ORDER BY data DESC"

            with conn.cursor() as cursor:
                cursor.execute(query, tuple(params))
                transactions = cursor.fetchall()
                transactions = [TransactionDatabase.format_transaction(row) for row in transactions]

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
    def get_categorias(idUser) -> list:
        """
        Retorna as categorias das transações do usuário.
        """       
        query = '''
            SELECT DISTINCT categoria FROM transactions
            WHERE idUser = %s;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
        
        return [categoria[0] for categoria in resultado]
    
    @staticmethod
    def get_mes_transacoes(idUser) -> list:
        """
        Retorna os meses que possuem transações registradas, formatados como 'Mon/YY' e 'YYYY-MM'.
        """       
        query = '''
            SELECT 
                TO_CHAR(data, 'Mon/YY') AS mes_ano,
                TO_CHAR(data, 'YYYY-MM') AS ano_mes
            FROM transactions 
            WHERE idUser = %s
            GROUP BY mes_ano, ano_mes
            ORDER BY MAX(data) ASC;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
        
        return [{'mes': mes_ano, 'ano_mes': ano_mes} for mes_ano, ano_mes in resultado]
    
    @staticmethod
    def get_transactions_categoria(idUser, categoria) -> list:
        """
        Retorna as transações filtradas por categoria.
        """       
        query = '''
            SELECT * FROM transactions 
            WHERE idUser = %s
            AND categoria = %s;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser, categoria))
                resultado = cursor.fetchall()
        
        return [TransactionDatabase.format_transaction(row) for row in resultado]
