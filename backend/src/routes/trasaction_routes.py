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

@router_transaction.route('/transacao_mes/id=<int:id>', methods=['GET'])
def get_transacoes_mes(id):
    transacoes = TransactionDatabase.get_all_transactions(id)

    # Usando OrderedDict para garantir a ordem dos meses
    transacoes_por_mes = defaultdict(float)

    for transacao in transacoes:
        data = transacao[5]  # Data da transação
        valor = transacao[4]  # Valor da transação

        valor = float(valor) if isinstance(valor, Decimal) else valor

        mes_nome = calendar.month_abbr[data.month].capitalize()  # Nome do mês (abreviado)
        
        transacoes_por_mes[mes_nome] += valor  

    # Ordenando por mês, mas invertendo os dados ao final da inserção
    meses_abreviados = list(calendar.month_abbr)[1:]  # Remove o valor vazio do índice 0
    transacoes_ordenadas = OrderedDict()

    # Inserir os dados de transações no OrderedDict já na ordem correta
    for mes in meses_abreviados:
        if mes in transacoes_por_mes:
            transacoes_ordenadas[mes] = transacoes_por_mes[mes]

    return jsonify(transacoes_ordenadas)

@router_transaction.route('/transacao_categoria/id=<int:id>', methods=['GET'])
def get_transacao_categoria(id):
    # Recupera todas as transações do usuário
    transacoes = TransactionDatabase.get_all_transactions(id)

    # Inicializa um dicionário para armazenar as somas das transações por categoria
    transacoes_por_categoria = defaultdict(float)
    total_transacoes = 0.0  # Variável para somar o valor total das transações

    # Processa cada transação
    for transacao in transacoes:
        categoria = transacao[2]  # Supondo que a categoria esteja na posição 2
        valor = transacao[4]  # Supondo que o valor da transação esteja na posição 4

        valor = float(valor) if isinstance(valor, Decimal) else valor

        # Soma o valor total
        total_transacoes += valor

        # Soma o valor por categoria
        transacoes_por_categoria[categoria] += valor

    # Calcula a porcentagem e o total gasto em cada categoria
    resultado_categoria = {}
    for categoria, valor in transacoes_por_categoria.items():
        porcentagem = (valor / total_transacoes) * 100
        porcentagem = round(porcentagem, 2)
        
        resultado_categoria[categoria] = {
            "total_gasto": valor,
            "porcentagem": porcentagem
        }

    # Retorna o resultado como JSON
    return jsonify(resultado_categoria)
