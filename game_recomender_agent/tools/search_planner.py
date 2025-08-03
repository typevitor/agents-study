from custom_agents.planner_agent import planner_agent

search_planner_tool = planner_agent.as_tool(
    tool_name="plan_searches",
    tool_description="Planeja pesquisas na web para responder a uma consulta.",
)