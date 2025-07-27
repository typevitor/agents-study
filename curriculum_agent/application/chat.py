from domain.agent import Agent
from domain.evaluator import Evaluator
from application.openai_provider import OpenAIProvider

class Chat:
    
    def __init__(self, name: str, curriculum: str, summary: str):
        self.openai_client = OpenAIProvider()
        self.agent = Agent(self.openai_client, name, curriculum, summary)
        self.evaluator = Evaluator(self.openai_client, name, curriculum, summary)

    def chat(self, message, history=[]):
        print(f"Messages: {message}", f"History: {history}")
        reply = self.agent.chat(message, history)
        evaluation = self.evaluator.evaluate(history, message, reply)
        
        while not evaluation.is_acceptable:
            print(f"Failed Evaluation: {evaluation.feedback}")
            reply = self.agent.rerun(reply, evaluation.feedback, message, history)
            evaluation = self.evaluator.evaluate(history, message, reply)

        print(f"Passed Evaluation: {evaluation.feedback}")
        return reply