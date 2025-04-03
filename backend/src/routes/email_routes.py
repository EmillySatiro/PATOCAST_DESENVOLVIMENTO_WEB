from flask import Blueprint, request, jsonify
from src.email.email_send import EmailSender
from src.email.email_body import criar_corpo_email_recupercao_de_conta_html
from src.database.user_database import UserDatabase
from os import getenv

# Inicializa o serviço de envio de e-mails
email_sender = EmailSender(getenv("EMAIL"), getenv("EMAIL_PASSWORD"))
email_routes = Blueprint('email_routes', __name__)

@email_routes.route('/email/recuperar_senha/', methods=['POST'])
def recuperar_senha():
    """
    Endpoint para recuperação de senha.
    Envia um e-mail ao usuário com instruções para recuperar a senha.
    """
    data = request.form.to_dict()
    email = data.get('email')
    
    if not email:
        return jsonify({"error": "Email is required"}), 400
    
    print(f"Recuperar senha para o email: {email}")
    try:
        email_sender.send_email(
            subject='Recuperação de Senha',
            to=email,
            body=criar_corpo_email_recupercao_de_conta_html(email=email)
        )
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@email_routes.route('/email/alteracao-senha/email=<string:email>', methods=['POST'])
def alterar_senha(email):
    """
    Endpoint para alteração de senha.
    Atualiza a senha do usuário no banco de dados.
    """
    data = request.form.to_dict()
    senha = data.get('senha')
    
    if not senha:
        return jsonify({"error": "Password is required"}), 400
    
    print(f"Alterar senha para o email: {email}")
    try:
        UserDatabase.update_user_password(email=email, password=senha)
        return jsonify({"message": "Password changed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
