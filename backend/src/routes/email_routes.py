from flask import Blueprint, request, jsonify
from src.email.email_send import EmailSender
from src.email.email_body import criar_corpo_email_recupercao_de_conta_html
from src.database.user_database import UserDatabase
from os import getenv

email_sender = EmailSender(getenv("EMAIL"), getenv("EMAIL_PASSWORD"))
email_routes = Blueprint('email_routes', __name__)

@email_routes.route(
    '/email/recuperar_senha/', methods=['POST']
)
def recuperar_senha():
    data = request.get_json()
    email = data['email']

    print(f"Recuperar senha para o email: {email}")
    try:
        email_sender.send_email(
            subject='Recuperação de Senha',
            to=email,
            body=criar_corpo_email_recupercao_de_conta_html(
                email=email
            )
        )
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@email_routes.route('/email/alteracao-senha/email=<string:email>', methods=['POST'])
def alterar_senha(email):
    data = request.get_json()
    senha = data['senha']
    
    print(f"Alterar senha para o email: {email}")
    
    print(f"Alterar senha para o email: {email}")
    try:
        UserDatabase.update_user_password(email=email, password=senha)
        return jsonify({"message": "Password changed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500