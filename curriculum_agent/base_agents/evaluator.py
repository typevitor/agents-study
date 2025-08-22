from pydantic import BaseModel
from application.openai_provider import OpenAIProvider

class Evaluation(BaseModel):
    is_acceptable: bool
    feedback: str

class Evaluator:
    def __init__(self, provider: OpenAIProvider, name: str, summary: str):
        self.openai_client = provider
        self.name = name
        self.summary = summary
    
    def system_prompt(self):
        return f"""Você está agindo como um avaliador entre a interação do cliente e o Modelo de IA.
            Sua tarefa é avaliar a resposta do modelo com base no contexto fornecido.
            O Agente está agindo como {self.name} e está respondendo perguntas sobre sua carreira, experiência, formação acadêmica, cursos, habilidades e projetos.
            O Agente foi instruído a ser profissional, educado e claro em suas respostas, como se estivesse conversando com futuros empregadores.
            O Agente recebeu o currículo e o sumário de {self.name} para auxiliar na resposta às perguntas.
        """
    
    def evaluate_user_prompt(self, history, message, reply):
        return f"""
            Aqui está o histórico da conversa:{history}
            Última mensagem do usuário: {message}
            Resposta do modelo: {reply}
            Avalie a resposta do modelo com base no contexto fornecido.
        """
    
    def evaluate(self, history, message, reply) -> Evaluation:
        messages = [{
            "role": "system", 
            "content": self.system_prompt()
        }] + [{
            "role": "user", 
            "content": self.evaluate_user_prompt(history, message, reply)
        }]
        return self.openai_client.send_message(
            messages=messages, 
            response_format=Evaluation
        )