import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Carregar variáveis do .env manualmente
def load_env():
    if os.path.exists('.env'):
        with open('.env', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

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

def send_test_email():
    # Carregar variáveis
    load_env()
    
    # Ler o HTML do arquivo
    print("📧 Carregando HTML do email...")
    with open('email-version.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Carregar lista de emails
    print("📋 Carregando lista de destinatários...")
    to_emails_list = load_email_list()
    
    if not to_emails_list:
        print("❌ ERRO: Nenhum email encontrado em emails_list.txt")
        print("   Adicione emails no arquivo emails_list.txt (um por linha)")
        return
    
    print(f"✅ {len(to_emails_list)} destinatário(s) encontrado(s):")
    for email in to_emails_list:
        print(f"   - {email}")
    
    # Pegar variáveis
    smtp_host = os.environ.get('SMTP_HOST')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')
    from_email = os.environ.get('FROM_EMAIL')
    
    print(f"\n✅ SMTP Host: {smtp_host}")
    print(f"✅ SMTP Port: {smtp_port}")
    print(f"✅ Usuário: {smtp_user}")
    print(f"✅ Senha: {'*' * len(smtp_password) if smtp_password else 'NÃO CONFIGURADA'}")
    print(f"✅ De: {from_email}")
    
    if not all([smtp_host, smtp_user, smtp_password, from_email]):
        print("\n❌ ERRO: Configure todas as variáveis no arquivo .env")
        return
    
    if smtp_password == 'SUA_SENHA_DO_EMAIL_AQUI':
        print("\n❌ ERRO: Você precisa substituir 'SUA_SENHA_DO_EMAIL_AQUI' pela senha real do seu email!")
        return
    
    subject = "💧 Lembrete Diário: Você é uma MÁQUINA DE VENCER! 💪"
    
    print(f"\n📬 Conectando ao servidor SMTP do Porkbun...")
    
    try:
        # Conectar ao servidor SMTP
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        
        print(f"🔐 Fazendo login...")
        server.login(smtp_user, smtp_password)
        
        print(f"✅ Login bem-sucedido!")
        
        # Enviar para cada destinatário
        for to_email in to_emails_list:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to_email
            
            html_part = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(html_part)
            
            print(f"📤 Enviando para {to_email}...")
            server.send_message(msg)
            print(f"✅ Email enviado para {to_email}!")
        
        server.quit()
        print("\n🎉 SUCESSO! Todos os emails foram enviados!")
        
    except smtplib.SMTPAuthenticationError:
        print("\n❌ ERRO: Falha na autenticação!")
        print("   Verifique se o email e senha estão corretos no .env")
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")

if __name__ == "__main__":
    print("🚀 Teste de Envio de Email via Porkbun SMTP\n")
    send_test_email()
    print("\n✨ Teste concluído! Verifique sua caixa de entrada (e spam).")
