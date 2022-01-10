import smtplib
import email.message

def enviar():

    email_escopo = """
            <p>email enviado por python</p>
            """

    msg = email.message.Message()
    msg['Subject'] = "assunto do email"
    msg['From'] = "usuario@gmail.com"
    msg['To'] = "usuario@gmail.com"
    senha = 'senha_do_email'
    
    msg.add_header('Content-type', 'text/html')
    msg.set_payload(email_escopo)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("o email foi enviado")

enviar()