import os
from openai import OpenAI

class OpenAIProvider:

    MODEL_NAME= "gpt-4o-mini"
    MAX_TOKENS = 1000
    TEMPERATURE = 0.3

    tools = []

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
        self.client = self.make()

    def make(self) -> OpenAI:
        return OpenAI(api_key=self.api_key)

    def send_message(self, messages, response_format=None):

        if response_format is not None:
            reply = self.client.beta.chat.completions.parse(
                model=self.MODEL_NAME, 
                messages=messages, 
                response_format=response_format
            )
            return reply.choices[0].message.parsed
        response = self.client.chat.completions.create(
            model=self.MODEL_NAME,
            messages=messages,
            max_tokens=self.MAX_TOKENS,
            temperature=self.TEMPERATURE,
            tools=self.tools,
        )
        message = response.choices[0].message
        print(f"Choices: {response.choices[0]}", flush=True)
        if(response.choices[0].finish_reason == "tool_calls"):
            return message.content, message.tool_calls
        return message.content, None

    def add_tool(self, tool):
        self.tools.append(tool)
        print(f"Tool added to OpenAIProvider.")
        