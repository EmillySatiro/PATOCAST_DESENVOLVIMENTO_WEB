from flask import Blueprint, jsonify, Response, request
import json
from src.database.transaction_database import TransactionDatabase

# Criação do blueprint para rotas relacionadas a transações
router_transaction = Blueprint('transacao', __name__)

@router_transaction.route('/transacao/', methods=['GET'])
def get_transacoes():
    """
    Obtém todas as transações de um usuário com base nos filtros opcionais.
    
    Parâmetros:
        id (int): ID do usuário cujas transações serão recuperadas (query param).
        mes (str, opcional): Mês para filtrar as transações.
        categoria (str, opcional): Categoria para filtrar as transações.
    
    Retorna:
        JSON contendo a lista de transações ou uma mensagem de erro.
    """
    idUser = request.args.get('id')
    mes = request.args.get('mes')
    categoria = request.args.get('categoria')
    
    transacoes = TransactionDatabase.get_all_transactions(idUser, mes, categoria)
    return Response(json.dumps(transacoes), mimetype='application/json')

@router_transaction.route('/get_categorias/id=<int:id>', methods=['GET'])
def get_categoria(id):
    """
    Obtém todas as categorias de transações de um usuário.
    
    Parâmetros:
        id (int): ID do usuário.
    
    Retorna:
        JSON contendo a lista de categorias.
    """
    transactions = TransactionDatabase.get_categorias(id)
    return Response(json.dumps(transactions), mimetype='application/json')

@router_transaction.route('/transacao_mes/id=<int:id>', methods=['GET'])
def get_transactions_mes(id):
    """
    Obtém as transações de um usuário agrupadas por mês.
    
    Parâmetros:
        id (int): ID do usuário.
    
    Retorna:
        JSON contendo as transações agrupadas por mês.
    """
    transactions = TransactionDatabase.get_mes_transacoes(id)
    return Response(json.dumps(transactions), mimetype='application/json')

@router_transaction.route('/lest_transacao_mes/id=<int:id>', methods=['GET'])
def get_lest_transactions(id):
    """
    Obtém as últimas transações do mês de um usuário.
    
    Parâmetros:
        id (int): ID do usuário.
    
    Retorna:
        JSON contendo as últimas transações do mês.
    """
    transactions = TransactionDatabase.get_lest_transactions_mes(id)
    return Response(json.dumps(transactions), mimetype='application/json')

@router_transaction.route('/transacao_categoria/id=<int:id>', methods=['GET'])
def get_lest_transactions_mes_categorial(id):
    """
    Obtém as últimas transações do mês de um usuário, filtradas por categoria.
    
    Parâmetros:
        id (int): ID do usuário.
    
    Retorna:
        JSON contendo as últimas transações do mês filtradas por categoria.
    """
    transactions = TransactionDatabase.get_lest_transactions_mes_categoria(id)
    return Response(json.dumps(transactions), mimetype='application/json')

@router_transaction.route('/transacao_next_transactions/id=<int:id>', methods=['GET'])
def get_next_transactions(id):
    """
    Obtém previsões de transações para o próximo mês de um usuário.
    
    Parâmetros:
        id (int): ID do usuário.
    
    Retorna:
        JSON contendo as transações previstas para o próximo mês.
    """
    transactions = TransactionDatabase.get_transactions_predict_next_mes(id)
    return Response(json.dumps(transactions), mimetype='application/json')

@router_transaction.route('/transacao_days_in_month/id=<int:id>', methods=['GET'])
def get_days_in_month(id):
    """
    Obtém as transações agrupadas por dia da semana no mês atual.
    
    Parâmetros:
        id (int): ID do usuário.
    
    Retorna:
        JSON contendo as transações agrupadas por dia da semana.
    """
    transactions = TransactionDatabase.get_transactions_days_in_current_week(id)
    return Response(json.dumps(transactions), mimetype='application/json')
