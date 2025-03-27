from flask import Blueprint, jsonify, request, redirect, make_response
from src.database.transaction_database import TransactionDatabase

router_transaction = Blueprint('transacao', __name__)

@router_transaction.route('/transacao/id=<int:id>', methods=['GET'])
def get_transacoes(id):
    transacoes = TransactionDatabase.get_all_transactions(id)
    transacoes = [TransactionDatabase.format_transaction(transacao) for transacao in transacoes]
    
    return jsonify(transacoes)