from application.openai_provider import OpenAIProvider

class Agent:
    def __init__(self, provider: OpenAIProvider, name: str, curriculum: str, summary: str):
        self.openai_client = provider
        self.name = name
        self.curriculum_text = curriculum
        self.summary = summary
    

    def system_prompt(self):
        return f"""
            Você está agindo como {self.name}, Você está respondendo perguntas no site do {self.name}.
            Particulamente respostas sobre a carrência, experiência, formação academica, cursos, habilidades e projetos.
            Sua responsabilidade é representar o {self.name} de forma profissional e precisa.
            Você  recebeu o currículo e o sumário de {self.name} para auxiliar na resposta às perguntas.
            Seja profissional, educado e claro em suas respostas. 
            Se você não souber a resposta, diga que não sabe e execute a ferramenta api_push_message
            Currículo: {self.curriculum_text}
            Sumário: {self.summary}
            Com esse contexto, por favor interaja com o usuário, sempre agindo como {self.name} e respondendo às perguntas de forma profissional e precisa.
        """

    def chat(self, message, history=[]):
        print(f"Messages: {message}", f"History: {history}")
        messages = [
            {"role": "system", "content": self.system_prompt()},
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
            "\n\n## Previous answer rejected\nYou just tried to reply, but the quality control rejected your reply.\n"
            f"## Your attempted answer:\n{original_reply}\n\n"
            f"## Reason for rejection:\n{feedback}\n"
        )
        messages = [
            {"role": "system", "content": updated_prompt}
        ] + history + [
            {"role": "user", "content": message}
        ]
        reply, tool_call = self.openai_client.send_message(messages)
        return reply, tool_call