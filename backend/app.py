from flask import Flask
from src.routes.user_routes import router_user

app = Flask(__name__)
app.register_blueprint(router_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)