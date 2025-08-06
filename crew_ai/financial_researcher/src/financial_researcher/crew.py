from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from typing import List

@CrewBase
class FinancialResearcher():
    """FinancialResearcher crew"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            verbose=True
        )
    
    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.analyst()],
            tasks=[self.research_task(), self.analysis_task()],
            process=Process.sequential,
            verbose=True
        )