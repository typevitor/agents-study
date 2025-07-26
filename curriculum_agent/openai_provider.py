import os
from openai import OpenAI

class OpenAIProvider:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    def make(self) -> OpenAI:
        return OpenAI(api_key=self.api_key) 