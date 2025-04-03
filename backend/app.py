"""
Flask Application

Este código implementa uma aplicação web usando Flask, organizando as rotas em diferentes Blueprints.
Além disso, utiliza Flask-CORS para permitir requisições de diferentes origens.

Dependências:
- Flask: Framework web para Python
- Flask-CORS: Permite requisições entre domínios
- python-dotenv: Carrega variáveis de ambiente de um arquivo .env

Estrutura do código:
1. Importação de módulos
2. Configuração do ambiente e carregamento de variáveis
3. Definição das rotas e Blueprints
4. Configuração e inicialização do aplicativo
"""

# Importação de módulos
from os import getenv
from dotenv import load_dotenv
load_dotenv()

# Importação de Blueprints das rotas
from flask import Flask, Blueprint
from flask_cors import CORS
from src.routes.user_routes import router_user
from src.routes.trasaction_routes import router_transaction
from src.routes.card_roules import card_routes  
from src.routes.email_routes import email_routes
from src.routes.form_routes import form_routes

# Carrega variáveis de ambiente
rout_teste = Blueprint('route', __name__)
@rout_teste.route('/', methods=['GET'])
def teste():
    return "Hello World"

# Inicialização da aplicação Flask
app = Flask(__name__)

# Registro dos Blueprints no aplicativo Flask
app.register_blueprint(rout_teste)
app.register_blueprint(router_user)
app.register_blueprint(router_transaction)
app.register_blueprint(card_routes)
app.register_blueprint(email_routes)
app.register_blueprint(form_routes)


# Habilita CORS para permitir chamadas de diferentes origens
CORS(app)

# Inicialização do servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
