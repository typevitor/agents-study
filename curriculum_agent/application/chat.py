import json
from domain.agent import Agent
from domain.evaluator import Evaluator
from application.openai_provider import OpenAIProvider
from application.api import Api

class Chat:
    
    def __init__(self, name: str, curriculum: str, summary: str):
        self.openai_client = OpenAIProvider()
        self.agent = Agent(self.openai_client, name, curriculum, summary)
        self.evaluator = Evaluator(self.openai_client, name, curriculum, summary)
        self.openai_client.add_tool(
            {"type": "function", "function": Api().tool_definition()}
        )

    def chat(self, message, history=[]):
        reply, tool_call = self.agent.chat(message, history)
        done = False
        while not done:
            if tool_call:
                print(f"Tool call detected: {tool_call}", flush=True)
                results = self.handle_tool_calls(tool_call)
                history.append({"role": "assistant", "content": reply})
                history.extend(results)
                reply, tool_call = self.agent.chat(message, history)
            else:
                done = True

        evaluation = self.evaluator.evaluate(history, message, reply)        
        while not evaluation.is_acceptable:
            print(f"Failed Evaluation: {evaluation.feedback}")
            reply = self.agent.rerun(reply, evaluation.feedback, message, history)
            evaluation = self.evaluator.evaluate(history, message, reply)

        print(f"Passed Evaluation: {evaluation.feedback}")
        return reply
    
    def handle_tool_calls(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool called: {tool_name}", flush=True)
            tool = globals().get(tool_name)
            result = tool(**arguments) if tool else {}
            results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
        return results