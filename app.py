from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'atendimento@rafaelprincipe.com.br'  # Seu e-mail
app.config['MAIL_PASSWORD'] = '1&acnTkr'    # Sua senha ou App Password
app.config['MAIL_DEFAULT_SENDER'] = 'atendimento@rafaelprincipe.com.br'

mail = Mail(app)


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


if __name__ == "__main__":
    app.run(debug=True)
