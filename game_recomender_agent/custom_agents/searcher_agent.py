from agents import Agent, WebSearchTool, ModelSettings

INSTRUCTIONS = f"""
Você é um dedicado **Agente de Pesquisa**. Sua tarefa é realizar pesquisas na web com base em consultas fornecidas.
Sumarize as informações encontradas em no máximo 300 palavras. Não inclua nenhum comentário ou explicação adicional, apenas o resumo.
"""

searcher_agent = Agent(
    name="SearcherAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[WebSearchTool(search_context_size="low")],
    model_settings=ModelSettings(tool_choice="required"),
)