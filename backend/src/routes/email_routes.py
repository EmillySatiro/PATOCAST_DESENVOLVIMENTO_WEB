from flask import Blueprint, request, jsonify
from src.email.email_send import EmailSender
from src.email.email_body import criar_corpo_email_recupercao_de_conta_html
from src.database.user_database import UserDatabase
from os import getenv

email_sender = EmailSender(getenv("EMAIL"), getenv("EMAIL_PASSWORD"))
email_routes = Blueprint('email_routes', __name__)

@email_routes.route('/email/recuperar_senha/id=<int:id>', methods=['POST'])
def send_email(id):
    
    user = UserDatabase.get_user_by_id(id)

    email = user['email']
    if not email:
        return jsonify({"error": "User does not have an email"}), 400
    
    new_password = UserDatabase.generate_new_password(id)
    
    try:
        email_sender.send_email(
            subject='Recuperação de Senha',
            to=email,
            body= criar_corpo_email_recupercao_de_conta_html(
                usuario=user['nome'],
                senha=new_password,
            )
        )
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
