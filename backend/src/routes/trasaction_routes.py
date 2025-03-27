from flask import Blueprint, jsonify
from src.database.transaction_database import TransactionDatabase
from collections import defaultdict
import calendar 
from decimal import Decimal
from collections import OrderedDict

router_transaction = Blueprint('transacao', __name__)

@router_transaction.route('/transacao/id=<int:id>', methods=['GET'])
def get_transacoes(id):
    transacoes = TransactionDatabase.get_all_transactions(id)
    transacoes = [TransactionDatabase.format_transaction(transacao) for transacao in transacoes]
    
    return jsonify(transacoes)

@router_transaction.route('/transacao_ultimas/id=<int:id>', methods=['GET'])
def get_lest_transactions(id):
    transactions = TransactionDatabase.get_lest_transactions_mes(id)
    return jsonify(transactions)


@router_transaction.route('/transacao_ultimas_categoria/id=<int:id>', methods=['GET'])
def get_lest_transactions_mes_categorial(id):
    transactions = TransactionDatabase.get_lest_transactions_mes_categoria(id)
    return jsonify(transactions)
