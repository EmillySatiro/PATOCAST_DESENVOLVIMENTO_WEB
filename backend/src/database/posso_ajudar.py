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