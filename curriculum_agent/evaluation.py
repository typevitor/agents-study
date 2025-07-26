from pydantic import BaseModel
from openai import OpenAI
import os

class Evaluation(BaseModel):
    is_acceptable: bool
    feedback: str

class Evaluator:
    def __init__(self, name, curriculum, summary):
        openai_key = os.getenv("OPENAI_API_KEY")
        self.openai_client = OpenAI(api_key=openai_key)
        self.name = name
        self.curriculum_text = curriculum
        self.summary = summary
    
    def system_prompt(self, name, curriculum_text, summary):
        return f"""Você está agindo como um avaliador entre a interação do cliente e o Modelo de IA.
            Sua tarefa é avaliar a resposta do modelo com base no contexto fornecido.
            O Agente está agindo como {name} e está respondendo perguntas sobre sua carreira, experiência, formação acadêmica, cursos, habilidades e projetos.
            O Agente foi instruído a ser profissional, educado e claro em suas respostas, como se estivesse conversando com futuros empregadores.
            O contexto é o currículo e o sumário de {name}.
            O Agente recebeu o currículo e o sumário de {name} para auxiliar na resposta às perguntas.
            Currículo: {curriculum_text}
            Sumário: {summary}
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
            "content": self.system_prompt(self.name, self.curriculum_text, self.summary)
        }] + [{
            "role": "user", 
            "content": self.evaluate_user_prompt(history, message, reply)
        }]
        response = self.openai_client.beta.chat.completions.parse(model="gpt-4o-mini", messages=messages, response_format=Evaluation)
        return response.choices[0].message.parsed
