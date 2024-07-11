import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_address, body):
    from_addr = 'lroojdvmktbo7gz7@ethereal.email'
    login = 'lroojdvmktbo7gz7@ethereal.email'
    password = 'x4sMTCzwv9t2bd7z7w'
    
    msg = MIMEMultipart()
    msg['from'] = "viagens_confirmar@email.com"
    msg['to'] = ', '.join(to_address)
    msg['subject'] = 'Confirmação de Viagem!'
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.ethereal.email', 587)
    server.starttls()
    server.login(login, password)
    
    text = msg.as_string()
    
    for email in to_address:
        server.sendmail(from_addr, email, text)
    server.quit()