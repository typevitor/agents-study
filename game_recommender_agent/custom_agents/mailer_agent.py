from agents import Agent
from tools.send_mail import send_email

HOW_MANY_SEARCHES = 5

INSTRUCTIONS = f"""
Você é um dedicado **Agente de Envio de Email**. Sua tarefa é enviar recomendações de jogos por email para os usuários.
Certifique-se de que o email esteja bem formatado, contenha todas as informações relevantes e seja enviado para o endereço fornecido.
Utilize a ferramenta `send_email` para enviar o email, incluindo o assunto, o endereço do destinatário e o corpo do email em Markdown.
"""

mailer_agent = Agent(
    name="MailerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[send_email],
)
