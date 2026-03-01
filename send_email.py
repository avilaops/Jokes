import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_email_list():
    """Carrega a lista de emails do arquivo emails_list.txt"""
    emails = []
    if os.path.exists('emails_list.txt'):
        with open('emails_list.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Ignora linhas vazias e comentários
                if line and not line.startswith('#'):
                    emails.append(line)
    return emails

def send_daily_reminder():
    # Ler o HTML do arquivo
    with open('email-version.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Carregar lista de destinatários
    to_emails = load_email_list()
    
    if not to_emails:
        print("ERRO: Nenhum email encontrado em emails_list.txt")
        return
    
    print(f"Enviando para {len(to_emails)} destinatário(s)...")
    
    # Pegar variáveis de ambiente
    smtp_host = os.environ.get('SMTP_HOST', 'smtp.porkbun.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')
    from_email = os.environ.get('FROM_EMAIL')
    
    subject = "💧 Lembrete Diário: Você é uma MÁQUINA DE VENCER! 💪"
    
    try:
        # Conectar ao servidor SMTP
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        
        # Enviar para cada destinatário
        for to_email in to_emails:
            to_email = to_email.strip()
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to_email
            
            html_part = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(html_part)
            
            server.send_message(msg)
            print(f"Email enviado para {to_email}!")
        
        server.quit()
        print("Todos os emails foram enviados com sucesso!")
        
    except Exception as e:
        print(f"Erro ao enviar email: {str(e)}")
        raise

if __name__ == "__main__":
    send_daily_reminder()
