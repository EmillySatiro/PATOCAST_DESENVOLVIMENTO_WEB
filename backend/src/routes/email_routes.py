from flask import Blueprint, request, jsonify
from src.email.email_send import EmailSender
from src.email.email_body import criar_corpo_email_recupercao_de_conta_html
from src.database.user_database import UserDatabase
from os import getenv

email_sender = EmailSender(getenv("EMAIL"), getenv("EMAIL_PASSWORD"))
email_routes = Blueprint('email_routes', __name__)


@email_routes.route(
    '/email/recuperar_senha/token=<string:token>', methods=['POST']
)
def recuperar_senha(token):
    data = request.form.to_dict()
    email = data['email']
    
    print(f"Recuperar senha para o email: {email} com token: {token}")
    try:
        email_sender.send_email(
            subject='Recuperação de Senha',
            to=email,
            body=criar_corpo_email_recupercao_de_conta_html(
                token=token,
                email=email
            )
        )
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
