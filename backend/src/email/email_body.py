
def criar_corpo_email_recupercao_de_conta_html(token, email):
    corpo_email = f"""
    <html>
    <head>
      <style>
      body {{
        font-family: Arial, sans-serif;
      }}
      .container {{
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        width: 80%;
        margin: 0 auto;
      }}
      .header {{
        background-color: #f2f2f2;
        padding: 10px;
        text-align: center;
        border-bottom: 1px solid #ccc;
      }}
      .content {{
        margin-top: 20px;
      }}
      .footer {{
        margin-top: 20px;
        text-align: center;
        font-size: 12px;
        color: #777;
      }}
      </style>
    </head>
    <body>
      <div class="container">
      <div class="header">
        <h2>Link de Recuperação de Senha</h2>
      </div>
      <div class="content">
        <p>Link para recuperação de senha:</p>
        <p><a href="http://localhost:3000/recuperar_senha/token={token}&email={email}">Clique aqui para redefinir sua senha</a></p>
      </div>
      <div class="footer">
        <p>Atenciosamente,</p>
        <p>Equipe de suporte</p>
      </div>
      </div>
    </body>
    </html>
    """
    return corpo_email


def criar_corpo_envio_arquivo_html():
    corpo_email = f"""
    <html>
    <head>
      <style>
      body {{
        font-family: Arial, sans-serif;
      }}
      .container {{
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        width: 80%;
        margin: 0 auto;
      }}
      .header {{
        background-color: #f2f2f2;
        padding: 10px;
        text-align: center;
        border-bottom: 1px solid #ccc;
      }}
      .content {{
        margin-top: 20px;
      }}
      .footer {{
        margin-top: 20px;
        text-align: center;
        font-size: 12px;
        color: #777;
      }}
      </style>
    </head>
    <body>
      <div class="container">
      <div class="header">
        <h2>Envio de Arquivos</h2>
      </div>
      <div class="content">
        <p>Segue em anexo os arquivos solicitados.</p>
      </div>
      <div class="footer">
        <p>Atenciosamente,</p>
        <p>Equipe de suporte</p>
      </div>
      </div>
    </body>
    </html>
    """
    return corpo_email
