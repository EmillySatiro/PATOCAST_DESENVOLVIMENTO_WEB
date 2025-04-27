from src.database.db import connection

class PossoAjudarDatabase:
    @staticmethod
    def format_posso_ajudar_data(posso_ajudar_tuple):
        return {
            'idPossoTeAjudar': posso_ajudar_tuple[0],
            'titulo': posso_ajudar_tuple[1],
            'descricao': posso_ajudar_tuple[2]
        }
    
    @staticmethod
    def get_all_posso_ajudar():
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM posso_te_ajudar")
                results = cursor.fetchall()
                results = [PossoAjudarDatabase.format_posso_ajudar_data(result) for result in results]
                return results
        return []
    
    @staticmethod
    def get_posso_ajudar(id):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM posso_te_ajudar WHERE idPossoTeAjudar = %s", (id,))
                result = cursor.fetchone()
                return PossoAjudarDatabase.format_posso_ajudar_data(result)
        return []
        
    @staticmethod
    def format_ajuda_content_data(ajuda_content_tuple):
        return {
            'idAjudaContent': ajuda_content_tuple[0],
            'idPossoTeAjudar': ajuda_content_tuple[1],
            'header_text': ajuda_content_tuple[2],
            'modal_cards': ajuda_content_tuple[3]
        }
    
    @staticmethod
    def get_all_ajuda_content(id):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM ajuda_content WHERE idPossoTeAjudar = %s", (id,))
                results = cursor.fetchall()
                results = [PossoAjudarDatabase.format_ajuda_content_data(result) for result in results]
                return results
        return []
    
    @staticmethod
    def posso_ajudar_recomendado(id):
        conn = connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""
                    WITH perfil AS (
                    SELECT
                        idUser,
                        CASE
                        WHEN (resposta->0->>'resposta') = '1' THEN 3 -- Planejar
                        WHEN (resposta->0->>'resposta') = '2' THEN 1 -- Economizar
                        WHEN (resposta->0->>'resposta') = '3' THEN 5 -- Entender
                        END AS objetivo,
                        
                        CASE
                        WHEN (resposta->1->>'resposta') = '1' THEN 8 -- Planejamento de aposentadoria (aposentado)
                        WHEN (resposta->1->>'resposta') = '2' THEN 9 -- Educação financeira básica (estudante)
                        WHEN (resposta->1->>'resposta') = '4' THEN 10 -- Empreender (PJ)
                        WHEN (resposta->1->>'resposta') IN ('5', '6') THEN 6 -- Sair das dívidas (negativado)
                        ELSE NULL
                        END AS perfil,

                        CASE
                        WHEN (resposta->2->>'resposta')::numeric < 2000 THEN 1 -- Economizar (baixa renda)
                        WHEN (resposta->2->>'resposta')::numeric BETWEEN 2000 AND 6000 THEN 7 -- Construir reserva de emergência
                        WHEN (resposta->2->>'resposta')::numeric > 6000 THEN 2 -- Investir (alta renda)
                        ELSE NULL
                        END AS renda
                    FROM respostas
                    WHERE idUser = {id}
                    )
                    SELECT DISTINCT ac.idpossoteajudar
                    FROM perfil p
                    JOIN posso_te_ajudar pa ON pa.idpossoteajudar IN (p.objetivo, p.perfil, p.renda)
                    JOIN ajuda_content ac ON ac.idPossoTeAjudar = pa.idpossoteajudar;
                """)
                results = cursor.fetchall()
                results = [id for (id,) in results]
                return results
        return []