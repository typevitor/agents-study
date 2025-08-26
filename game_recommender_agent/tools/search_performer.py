from agents import Runner, function_tool
from custom_agents.planner_agent import WebSearchPlan, WebSearchItem
from custom_agents.searcher_agent import searcher_agent
import asyncio

@function_tool
async def perform_search_tool(search_plan: WebSearchPlan) -> list[str]:
    """ Perform the searches to perform for the query """
    print("Pesquisando...")
    num_completed = 0
    tasks = [asyncio.create_task(search(item)) for item in search_plan.searches]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        if result is not None:
            results.append(result)
        num_completed += 1
        print(f"Searching... {num_completed}/{len(tasks)} completed")
    print("Finished searching")
    return results

async def search(item: WebSearchItem) -> str | None:
    """ Perform a search for the query """
    input = f"Search term: {item.query}\nReason for searching: {item.reason}"
    try:
        result = await Runner.run(
            searcher_agent,
            input,
        )
        return str(result.final_output)
    except Exception:
        return None
