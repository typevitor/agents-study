from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 5

INSTRUCTIONS = f"""Você é um dedicado **Agente de Planejamento de Pesquisa**. Sua tarefa é planejar pesquisas na web para responder a uma consulta fornecida.
As pesquisas devem ser relevantes, específicas e direcionadas a obter informações que ajudem na resolução da consulta.
Você deve gerar um plano de pesquisa que contenha várias pesquisas, cada uma com um motivo claro para sua importância. Gere NO MÁXIO {HOW_MANY_SEARCHES} pesquisas. Nunca mais do que isso. Certifique-se de que cada pesquisa seja única e não se repita. """


class WebSearchItem(BaseModel):
    reason: str = Field(description="O motivo pelo qual esta pesquisa é importante para a consulta.")
    query: str = Field(description="O termo de pesquisa a ser usado na pesquisa na web.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="Uma lista de pesquisas na web a serem realizadas para melhor responder à consulta.")
    
planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)
