from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Coder():
    """Coder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def coder(self) -> Agent:
        """Creates a Coder agent"""
        return Agent(
            config=self.agents_config['coder'],
            verbose=True,
            allow_code_execution=True,  # Allows the agent to execute code
            code_execution_mode="safe",
            max_execution_time=60,
            max_retry_limit=3
        )
    
    @task
    def write_python_code(self) -> Task:
        """Creates a Coder task"""
        return Task(config=self.tasks_config['write_python_code'])

    @crew
    def crew(self) -> Crew:
        """Creates the Coder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
