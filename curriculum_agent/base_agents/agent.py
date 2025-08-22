from application.openai_provider import OpenAIProvider
from application.db import ChromaDB

class Agent:
    def __init__(self, provider: OpenAIProvider, name: str, summary: str):
        self.openai_client = provider
        self.name = name
        self.summary = summary
        self.db = ChromaDB()
    

    def system_prompt(self, original_message):
        results = self.db.similarity_search_with_score(original_message, k=3)
        print(f"Resultado do RAG: {results}")
        prompt = f"""
            Você está agindo como {self.name}, Você está respondendo perguntas no site do {self.name}.
            Particulamente respostas sobre a carrência, experiência, formação academica, cursos, habilidades e projetos.
            Sua responsabilidade é representar o {self.name} de forma profissional e precisa.
            Você  recebeu o currículo e o sumário de {self.name} para auxiliar na resposta às perguntas.
            Seja profissional, educado e claro em suas respostas. 
            Se você não souber a resposta, diga que não sabe e execute a ferramenta api_push_message
            Sumário: {self.summary}
            Dados do Currículo: {results}
            Com esse contexto, por favor interaja com o usuário, sempre agindo como {self.name} e respondendo às perguntas de forma profissional e precisa.
        """
        return prompt

    def chat(self, message, history=[]):
        print(f"Messages: {message}", f"History: {history}")
        messages = [
            {"role": "system", "content": self.system_prompt(message)},
        ] + history + [
            {"role": "user", "content": message}
        ]
        reply, tool_call = self.openai_client.send_message(messages)
        print(f"chat Response: {reply}")
        return reply, tool_call

    def rerun(self, original_reply, feedback, message, history=[]):
        print(f"Messages: {message}", f"History: {history}")
        updated_prompt = self.system_prompt()
        updated_prompt += (
            "\n\n## Sua resposta anterior foi rejeitada\nVocê acabou de tentar responder, mas o agente avaliador rejeitou sua resposta.\n"
            f"## Sua resposta tentativa:\n{original_reply}\n\n"
            f"## Motivo da rejeição:\n{feedback}\n"
        )
        messages = [
            {"role": "system", "content": updated_prompt}
        ] + history + [
            {"role": "user", "content": message}
        ]
        reply, tool_call = self.openai_client.send_message(messages)
        return reply, tool_call