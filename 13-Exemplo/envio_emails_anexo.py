import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar():
    corpo =  """ olá este é um email enviando em python com anexo """

    remetente = 'usuario0@gmail.com'
    senha = 'senha_do_gmail'
    destinatario = 'email_de_destino@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subjetct'] = 'email com enexo'

    msg.attach(MIMEText(corpo, 'plain'))

    pdf = 'arquivo.pdf'

    b_pdf = open(pdf, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdf)
    payload.set_payload((b_pdf).read())

    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition', 'attachment', filename=pdf)
    msg.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()

    session.login(remetente, senha)

    texto = msg.as_string()
    session.sendmail(remetente, destinatario, texto)
    session.quit()
    print("email enviado com sucesso")

enviar()