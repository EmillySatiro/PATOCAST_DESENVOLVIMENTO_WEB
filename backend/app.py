from flask import Flask, jsonify, request
import psycopg2
from time import sleep

class Banco:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.conectar()
        
    def conectar(self):
        while True:
            try:
                self.connection = psycopg2.connect(
                    user="root",
                    password="root",
                    host="postgres",
                    port="5432",
                    database="patocash"
                )
                self.cursor = self.connection.cursor()
                print("Conectado ao banco de dados!")
                break
            except:
                print("Erro ao conectar com o banco de dados. Tentando novamente em 2 segundos...")
                sleep(2)
            
    def cadastrar(self, nome, sobrenome, email, senha):
        self.cursor.execute(f"INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('{nome}', '{sobrenome}', '{email}', '{senha}')")
        self.connection.commit()
    
    def get_user_por_id(self, id):
        self.cursor.execute(f"SELECT * FROM users WHERE idUser = {id}")
        return self.cursor.fetchone()
    
app = Flask(__name__)
banco = Banco()

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/api/cadastrar', methods=['POST'])
def cadastro():
    dados = request.form.to_dict()
    print(dados)
    banco.cadastrar(dados['nome'], dados['sobrenome'], dados['email'], dados['senha'])
    return jsonify({"mensagem": "Cadastro realizado com sucesso!", "dados": dados})

@app.route('/api/usuario/<int:id>', methods=['GET'])
def get_cartao(id):
    usuario = banco.get_user_por_id(id)
    return jsonify(usuario)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)