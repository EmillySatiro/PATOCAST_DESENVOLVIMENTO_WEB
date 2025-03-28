from flask import Blueprint, jsonify, Response, request
import json
from src.database.relatorio_database import RelatorioDatabase

router_relatorio = Blueprint('relatorio', __name__)

@router_relatorio.route('/relatorio/id=<int:id>', methods=['GET'])
def get_relatorio(id):
    data_inicio = '2025-01-01'
    data_fim = '2025-12-31'
    
    # Chama a função para pegar o relatório de gastos do usuário
    relatorio = RelatorioDatabase.get_relatorio(id, data_inicio, data_fim)
    if not relatorio:
        return jsonify({"error": "Relatório não encontrado"}), 404
    
    return Response(
        json.dumps(relatorio), 
        mimetype='application/json'
    )