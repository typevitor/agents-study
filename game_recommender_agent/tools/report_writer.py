from agents import Runner, function_tool
from custom_agents.writer_agent import writer_agent, ReportData

@function_tool
async def report_writer_tool(query: str, search_results: list[str]) -> str:
    """ Write the report for the query """
    print("Thinking about report...")
    input = f"Original query: {query}\nResumo da pesquisa: {search_results}"
    result = await Runner.run(
        writer_agent,
        input,
    )

    print("Finalizando pesquisa...")
    return result.final_output_as(ReportData)
    