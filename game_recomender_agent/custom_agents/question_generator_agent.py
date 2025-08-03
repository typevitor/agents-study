from agents import Agent

INSTRUCTIONS = f"""Você é um dedicado **Agente de Geração de Perguntas**. Sua tarefa é gerar perguntas relevantes com base em uma consulta fornecida. 
As perguntas devem ser claras, concisas e direcionadas a obter informações específicas que ajudem na compreensão ou resolução da consulta."""

question_generator_agent = Agent(
    name="QuestionGeneratorAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
)