from flask import Flask
from flask_cors import CORS
from src.routes.user_routes import router_user
from src.routes.trasaction_routes import router_transaction
from src.routes.card_roules import card_routes
# from src.routes.relatorio_routes import router_relatorio
from dotenv import load_dotenv
from os import getenv

if getenv("DOCKER_ENV") == None:
    load_dotenv()

app = Flask(__name__)
app.register_blueprint(router_user)
app.register_blueprint(router_transaction)
app.register_blueprint(card_routes)
# app.register_blueprint(router_relatorio)

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)