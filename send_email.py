import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

def send_daily_reminder():
    # Ler o HTML do arquivo
    with open('email-version.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Configurar email
    from_email = Email(os.environ.get('FROM_EMAIL'))  # Seu email
    to_emails = os.environ.get('TO_EMAILS').split(',')  # Lista de emails separados por vírgula
    
    # Criar lista de destinatários
    to_list = [To(email.strip()) for email in to_emails]
    
    subject = "💧 Lembrete Diário: Você é uma MÁQUINA DE VENCER! 💪"
    
    content = Content("text/html", html_content)
    
    # Criar mensagem
    for to_email in to_list:
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )
        
        try:
            # Enviar email
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(f"Email enviado para {to_email}! Status: {response.status_code}")
        except Exception as e:
            print(f"Erro ao enviar para {to_email}: {str(e)}")

if __name__ == "__main__":
    send_daily_reminder()
