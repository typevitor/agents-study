from agents import Runner, function_tool
from custom_agents.question_generator_agent import question_generator_agent  

@function_tool
async def question_generator(query: str, quantity: int) -> str:
    f""" Generate {quantity} questions to answer for the query """
    print("Generating questions...")
    result = await Runner.run(
        question_generator_agent,
        f"Query: {query}",
    )
    print(f"Generated {quantity} questions...")
    return result.final_output
    