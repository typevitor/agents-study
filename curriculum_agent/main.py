from dotenv import load_dotenv
from openai import OpenAI
from file_reader import FileReader
import os
import gradio as gr
from evaluation import Evaluator

load_dotenv(override=True)

openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")


reader = FileReader("curriculum_agent/data/me.pdf");
curriculum_text = reader.read_pdf();

with open("curriculum_agent/data/summary.txt", "r", encoding="utf-8") as filesummary:
    summary = filesummary.read()

openai_client = OpenAI(api_key=openai_key)

name = "Vitor A. Leal"
system_prompt = f"""
Você está agindo como {name}, Você está respondendo perguntas no site do {name}.
Particulamente respostas sobre a carrência, experiência, formação academica, cursos, habilidades e projetos.
Sua responsabilidade é representar o {name} de forma profissional e precisa.
Você  recebeu o currículo e o sumário de {name} para auxiliar na resposta às perguntas.
Seja profissional, educado e claro em suas respostas. 
Se você não souber a resposta, diga que não sabe.
Currículo: {curriculum_text}
Sumário: {summary}
Com esse contexto, por favor interaja com o usuário, sempre agindo como {name} e respondendo às perguntas de forma profissional e precisa.
"""

evaluator = Evaluator(name, curriculum_text, summary)

def chat(message, history=[]):
    print(f"Messages: {message}", f"History: {history}")
    messages = [
        {"role": "system", "content": system_prompt},
    ] + history + [{"role": "user", "content": message}]
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000,
        temperature=0.3
    )
    reply = response.choices[0].message.content

    evaluation = evaluator.evaluate(history, message, reply)
    if evaluation.is_acceptable:
        print(f"Passed Evaluation: {evaluation.feedback}")
        return reply
    
    print(f"Failed Evaluation: {evaluation.feedback}")
    return rerun(reply, evaluation.feedback, message, history)

def rerun(original_reply, feedback, message, history=[]):
    print(f"Messages: {message}", f"History: {history}")
    updated_prompt = system_prompt
    updated_prompt += (
        "\n\n## Previous answer rejected\nYou just tried to reply, but the quality control rejected your reply.\n"
        f"## Your attempted answer:\n{original_reply}\n\n"
        f"## Reason for rejection:\n{feedback}\n"
    )
    messages = [{"role": "system", "content": updated_prompt}] + history + [{"role": "user", "content": message}]
    response = openai_client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(chat, type="messages").launch()