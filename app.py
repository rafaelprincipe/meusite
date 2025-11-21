import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    data = {
        "sender": {"name": "Site Rafael", "email": os.getenv("MAIL_USERNAME")},
        "to": [{"email": os.getenv("MAIL_USERNAME")}],
        "subject": f"Nova mensagem do site - {nome}",
        "htmlContent": f"""
        <p><strong>Nome:</strong> {nome}</p>
        <p><strong>E-mail:</strong> {email}</p>
        <p><strong>Mensagem:</strong><br>{mensagem}</p>
        """
    }

    response = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": os.getenv("MAIL_API_KEY")
        },
        json=data
    )

    if response.status_code in [200, 201]:
        return "Mensagem enviada com sucesso!"
    else:
        return f"Erro ao enviar: {response.text}"



'from flask import Flask, render_template'

'app = Flask(__name__)'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/areas")
def areas():
    return render_template("areas.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form.get('telefone', 'Não informado')
    mensagem = request.form['mensagem']

    msg = Message(
        subject=f"Novo contato de {nome}",
        recipients=['rafael@rafaelprincipe.com.br']  # E-mail que vai receber
    )
    msg.body = f"""
    Novo contato recebido:

    Nome: {nome}
    Email: {email}
    Telefone: {telefone}
    Mensagem: {mensagem}
    """

    mail.send(msg)
    return render_template('/confirmacao.html', nome=nome)






