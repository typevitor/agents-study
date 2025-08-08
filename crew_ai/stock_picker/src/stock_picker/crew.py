from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from .tools.pusher_tool import PusherNotificationTool


from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

class TrendingCompany(BaseModel):
    name: str = Field(description="Name of the trending company")
    ticker: str = Field(description="Ticker symbol of the trending company")
    reason: str = Field(description="Reason for the company's trend")

class TrendingCompanyList(BaseModel):
    companies: List[TrendingCompany] = Field(
        description="List of trending companies with their details"
    )

class TrendingCompanyResearch(BaseModel):
    """Research on trending companies"""
    name: str = Field(
        description="Name of the company being researched"
    )
    market_position: str = Field(
        description="Market position of the company"
    )
    future_outlook: str = Field(
        description="Future outlook of the company"
    )
    investment_potential: str = Field(
        description="Investment potential and suitability for investment"
    )

class TrendingCompanyResearchList(BaseModel):
    """List of research on trending companies"""
    researches: List[TrendingCompanyResearch] = Field(
        description="List of research results for trending companies"
    )

@CrewBase
class StockPicker():
    """StockPicker crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'], 
            verbose=True,
            tools=[SerperDevTool()],
            memory=True
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'],
            verbose=True,
            tools=[PusherNotificationTool()],
            memory=True
        )

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'],
            output_pydantic=TrendingCompanyList,
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'],
            output_pydantic=TrendingCompanyResearchList
        )
    
    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company']
        )

    @crew
    def crew(self) -> Crew:

        manager = Agent(
            config=self.agents_config['manager'],
            allow_delegation=True,
        )

        short_term_memory = ShortTermMemory(
            storage=RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {
                        "model": "text-embedding-3-small",
                    }
                },
                type="short_term",
                path="./memory/"
            ),
        )

        long_term_memory = LongTermMemory(
            storage=LTMSQLiteStorage(
                db_path="./memory/long_term_memory_ltm.db",
            )
        )

        entity_memory = EntityMemory(
            storage=RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {
                        "model": "text-embedding-3-small",
                    }
                },
                type="short_term",
                path="./memory/",
            ),
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
            memory=True,
            short_term_memory=short_term_memory,
            long_term_memory=long_term_memory,
            entity_memory=entity_memory,
        )
