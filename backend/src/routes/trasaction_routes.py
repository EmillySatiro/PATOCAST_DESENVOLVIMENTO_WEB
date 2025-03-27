from flask import Blueprint, jsonify, Response
import json
from src.database.transaction_database import TransactionDatabase

router_transaction = Blueprint('transacao', __name__)

@router_transaction.route('/transacao/id=<int:id>', methods=['GET'])
def get_transacoes(id):
    transacoes = TransactionDatabase.get_all_transactions(id)
    transacoes = [TransactionDatabase.format_transaction(transacao) for transacao in transacoes]
    
    
    return Response(
            json.dumps(transacoes), 
            mimetype='application/json'
    )

@router_transaction.route('/transacao_mes/id=<int:id>', methods=['GET'])
def get_lest_transactions(id):
    transactions = TransactionDatabase.get_lest_transactions_mes(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )


@router_transaction.route('/transacao_categoria/id=<int:id>', methods=['GET'])
def get_lest_transactions_mes_categorial(id):
    transactions = TransactionDatabase.get_lest_transactions_mes_categoria(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )

@router_transaction.route('/transacao_next_transactions/id=<int:id>', methods=['GET'])
def get_next_transactions(id):
    transactions = TransactionDatabase.get_transactions_predict_next_mes(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )

@router_transaction.route('/transacao_days_in_month/id=<int:id>', methods=['GET'])
def get_days_in_month(id):
    transactions = TransactionDatabase.get_transactions_days_in_current_week(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )