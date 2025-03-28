from src.database.db import connection

# CREATE TABLE IF NOT EXISTS users (
#   idUser SERIAL PRIMARY KEY,  -- Auto incremento
#   nome VARCHAR(255) NOT NULL,
#   sobrenome VARCHAR(255) NOT NULL,
#   email VARCHAR(255) NOT NULL UNIQUE,
#   senha TEXT NOT NULL,
#   limite DECIMAL(10, 2) NOT NULL,
#   criado TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Data e hora de criação
#   atualizado TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP  -- Data e hora da última atualização
# );

# -- Criação da tabela 'transactions'
# CREATE TABLE IF NOT EXISTS transactions (
#   idTransaction SERIAL PRIMARY KEY,  -- Auto incremento
#   idUser INT NOT NULL,
#   estabelecimento VARCHAR(255) NOT NULL,
#   categoria VARCHAR(255) NOT NULL,
#   valor DECIMAL(10, 2) NOT NULL,
#   data DATE NOT NULL,
#   CONSTRAINT fk_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
# );

# -- Criação da tabela 'cartao'
# CREATE TABLE IF NOT EXISTS cartao (
#   idCartao SERIAL PRIMARY KEY,  -- Auto incremento
#   idUser INT NOT NULL,
#   numero VARCHAR(255) NOT NULL,
#   nome VARCHAR(255) NOT NULL,
#   meta DECIMAL(10, 2) NOT NULL,
#   tipo VARCHAR(255) NOT NULL,
#   CONSTRAINT fk_cartao_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
# );

# dados = {
#       nome: 'Jonas',
#       sobrenome: 'Silva',
#       data_inicio: '01/03/2025',
#       data_fim: '30/03/2025',
#       gastos_maiores: [
#           { local: 'Supermercado', categoria: 'Alimentação', data: '05/03/2025', valor: 150.50 },
#           { local: 'Restaurante', categoria: 'Alimentação', data: '10/03/2025', valor: 200.75 },
#       ],
#       gasto_total: 350.00,
#       gastos: [
#           { local: 'Supermercado', categoria: 'Alimentação', data: '01/03/2025', valor: 50.00 },
#           { local: 'Restaurante', categoria: 'Alimentação', data: '03/03/2025', valor: 80.00 },
#       ],
#   };


class RelatorioDatabase:

    @staticmethod
    def format_relatorio(relatorio_tuple):
        '''
        Formata os dados do relatório retornados pelo banco de dados.
        O formato esperado é uma tupla com os seguintes campos:
        
        - nome (str): Nome do usuário
        - sobrenome (str): Sobrenome do usuário
        - data_inicio (str): Data de início do relatório
        - data_fim (str): Data de fim do relatório
        - gasto_total (float): Total gasto pelo usuário
        - gastos_maiores (list): Lista de gastos maiores
        - gastos (list): Lista de gastos do usuário
        '''
        return {
            'nome': relatorio_tuple[0],
            'sobrenome': relatorio_tuple[1],
            'data_inicio': relatorio_tuple[2],
            'data_fim': relatorio_tuple[3],
            'gasto_total': float(relatorio_tuple[4]),
            'gastos_maiores': relatorio_tuple[5],
            'gastos': relatorio_tuple[6]
        }
    