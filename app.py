from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        smtp_server = 'SEU_SERVIDOR_SMTP'  # Substitua pelo endereço do seu servidor SMTP
        smtp_port = 587  # Substitua pela porta do seu servidor SMTP
        smtp_username = 'SEU_EMAIL'  # Substitua pelo seu endereço de e-mail
        smtp_password = 'SUA_SENHA'  # Substitua pela sua senha de e-mail

        # Configuração da mensagem
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = 'SEU_EMAIL_DESTINO'  # Substitua pelo seu endereço de e-mail de destino
        msg['Subject'] = assunto

        # Adiciona o corpo da mensagem
        msg.attach(MIMEText(f'Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\n\n{mensagem}', 'plain'))

        # Conecta-se ao servidor SMTP e envia o e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(email, 'SEU_EMAIL_DESTINO', msg.as_string())  # Substitua pelo seu endereço de e-mail de destino

        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
