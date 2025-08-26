from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = f"""
Você é um pesquisador de jogos senior com a tarefa de escrever um relatório para uma pesquisa de recomendação de jogos.
Você receberá a consulta original e os resultados da pesquisa realizada pelo agente de pesquisa.
Seu trabalho é escrever a lista de recomendação detalhando os prós e contras dos jogos pesquisados, e também fornecer um resumo curto da pesquisa. 
"""


class ReportData(BaseModel):
    pros: str = Field(description="Os prós dos jogos pesquisados.")
    cons: str = Field(description="Os contras dos jogos pesquisados.")
    veredict: str = Field(description="O veredicto final do relatório.")

writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)