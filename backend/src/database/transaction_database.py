from src.database.db import connection

class TransactionDatabase:

    @staticmethod
    def format_transaction(transaction_tuple):
        return {
            "idTransaction": transaction_tuple[0],
            "idUser": transaction_tuple[1],
            "estabelecimento": transaction_tuple[2],
            "categoria": transaction_tuple[3],
            "valor": float(transaction_tuple[4]),
            "data": transaction_tuple[5].strftime("%d/%m/%Y")
        }
    
    @staticmethod
    def get_all_transactions(idUser, mes=None, categoria=None) -> tuple:
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

            # Aplicar filtro de categoria, se fornecido
            if categoria and categoria != 'todas':
                query += " AND categoria = %s"
                params.append(categoria)

            # Ordenar por data, do mais recente para o mais antigo
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
                if(not resultado):
                    return {
                        'pendente': 0.0
                    }
                    
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
    def get_categorias(idUser) -> dict:
        """
        Retorna as categorias de acordo com o mes escolhido pelo usuario.
        """       
        query = '''
            SELECT categoria FROM transactions
            WHERE idUser = %s
            AND data <= NOW()
            GROUP BY categoria;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
        
        resultado = [categoria[0] for categoria in resultado]
        
        return resultado
    
    @staticmethod
    def get_mes_transacoes(idUser) -> dict:
        """
            Retorna os meses que têm transações do usuário no formato 'Mon/YY' 
            e o correspondente 'YYYY-MM' para ser usado na pesquisa.
        """       
        query = '''
            SELECT 
                TO_CHAR(data, 'Mon/YY') AS mes_ano,
                TO_CHAR(data, 'YYYY-MM') AS ano_mes
            FROM transactions 
            WHERE idUser = %s
            AND data <= NOW()
            GROUP BY mes_ano, ano_mes
            ORDER BY MAX(data) ASC;
        '''
        
        resultado_final = {}

        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,))
                resultado = cursor.fetchall()
                # Formatar o resultado conforme desejado
                resultado_final = [{'mes': mes_ano, 'ano_mes': ano_mes} for mes_ano, ano_mes in resultado]

        return resultado_final
    
    @staticmethod
    def get_transactions_categoria(idUser,categoria,mes) -> dict:
        """
        Retorna as transacoes de acordo com a categoria escolhida pelo usuario e pelo mes.
        """       
        
        query = '''
            SELECT * FROM transactions 
            WHERE idUser = %s
            AND categoria = %s
            AND data >= NOW() - INTERVAL '1 months'
            GROUP BY dia;
        '''
        
        with connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (idUser,categoria))
                resultado = cursor.fetchall()
                
        return resultado
    
    # @staticmethod
    # def get_all_transactions_mes(idUser,mes) -> dict:
    #     """
    #     Retorna todas as transacoes de acordo com o mes escolhido pelo usuario.
    #     """       
        
    #     query = '''
    #         SELECT *
    #         FROM transactions 
    #         WHERE idUser = %s
    #         AND TO_CHAR(data, 'YYYY-MM') = %s;

    #     '''
        
    #     with connection() as conn:
    #         with conn.cursor() as cursor:
    #             cursor.execute(query, (idUser,mes))
    #             resultado = cursor.fetchall()
    #             resultado = [TransactionDatabase.format_transaction(row) for row in resultado]
    #     return resultado