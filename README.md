# 📧 Automação de Email Diário - Máquina de Vencer

Este projeto envia automaticamente um email motivacional todos os dias às 15h (horário de Brasília).

## 🚀 Como Configurar

### 1️⃣ Criar Conta no SendGrid (GRÁTIS)

1. Acesse: https://signup.sendgrid.com/
2. Crie uma conta gratuita (100 emails/dia grátis)
3. Verifique seu email
4. Complete o Single Sender Verification:
   - Dashboard → Settings → Sender Authentication
   - Verify Single Sender
   - Preencha com seu email

### 2️⃣ Criar API Key no SendGrid

1. No SendGrid: Settings → API Keys
2. Clique em **Create API Key**
3. Nome: `GitHub Actions Daily Email`
4. Permissões: **Full Access** (ou Mail Send)
5. Clique em **Create & View**
6. **COPIE A API KEY** (você não verá ela novamente!)
   - Exemplo: `SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 3️⃣ Configurar Secrets no GitHub

1. Vá para seu repositório: https://github.com/avilaops/Jokes
2. Clique em **Settings** (configurações do repositório)
3. No menu lateral: **Secrets and variables** → **Actions**
4. Clique em **New repository secret**

Adicione os seguintes secrets:

#### Secret 1: SENDGRID_API_KEY
- **Name:** `SENDGRID_API_KEY`
- **Value:** Cole a API Key que você copiou do SendGrid
- Clique em **Add secret**

#### Secret 2: FROM_EMAIL
- **Name:** `FROM_EMAIL`
- **Value:** Seu email (o mesmo que verificou no SendGrid)
  - Exemplo: `seuemail@gmail.com`
- Clique em **Add secret**

#### Secret 3: TO_EMAILS
- **Name:** `TO_EMAILS`
- **Value:** Emails que vão receber (separados por vírgula)
  - Exemplo: `email1@gmail.com,email2@gmail.com,email3@gmail.com`
  - Ou apenas um: `seu.email@gmail.com`
- Clique em **Add secret**

### 4️⃣ Ativar GitHub Actions

1. No repositório, vá em **Actions**
2. Se aparecer para habilitar workflows, clique em **"I understand my workflows, go ahead and enable them"**
3. Você verá o workflow: **"Enviar Email Diário - Máquina de Vencer"**

### 5️⃣ Testar Manualmente (Antes de Esperar até as 15h!)

1. Vá em **Actions** no repositório
2. Clique em **"Enviar Email Diário - Máquina de Vencer"**
3. Clique em **"Run workflow"** → **"Run workflow"**
4. Aguarde alguns segundos
5. Verifique seu email! 📧

## ⏰ Horário

- **Agendamento:** Todo dia às **15:00** (horário de Brasília - BRT/UTC-3)
- **Como funciona:** GitHub Actions usa UTC, configurei para 18:00 UTC que equivale a 15:00 BRT

### Ajustar Horário (Opcional)

Para mudar o horário, edite o arquivo `.github/workflows/send-daily-email.yml`:

```yaml
- cron: '0 18 * * *'  # Minuto Hora * * *
```

**Exemplos:**
- 13:00 BRT (16:00 UTC): `'0 16 * * *'`
- 09:00 BRT (12:00 UTC): `'0 12 * * *'`
- 20:00 BRT (23:00 UTC): `'0 23 * * *'`

## 🎯 Resultado

A partir de agora, todos os dias às 15h, os emails configurados receberão:
- ✅ Lembrete motivacional do Capitão América
- ✅ Dicas de hidratação
- ✅ Mensagem: "Você é uma MÁQUINA DE VENCER!"

## 💰 Custo

**R$ 0,00** - Totalmente gratuito!
- SendGrid: 100 emails/dia grátis
- GitHub Actions: 2.000 minutos/mês grátis (este workflow usa ~30 segundos/dia)

## 🔍 Verificar Logs

Para ver se o email foi enviado:
1. **Actions** → **Enviar Email Diário - Máquina de Vencer**
2. Clique na execução mais recente
3. Veja os logs de **"Enviar email"**

## ❓ Problemas Comuns

### Email não chegou?
1. Verifique a pasta de **Spam/Lixo Eletrônico**
2. Verifique se o FROM_EMAIL está verificado no SendGrid
3. Veja os logs no GitHub Actions

### Erro "Unauthorized"?
- Verifique se a SENDGRID_API_KEY está correta
- Certifique-se que a API Key tem permissão "Mail Send"

### Erro "The from email does not match a verified sender"?
- Você precisa verificar o email no SendGrid (Single Sender Verification)

---

**🎉 Pronto! Agora você terá lembretes diários para se manter hidratado e ser uma MÁQUINA DE VENCER! 💪💧**
