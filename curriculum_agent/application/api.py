class Api:
    def __init__(self):
        self.name = "api_push_message"
        self.description = "Always use this tool to record any question that couldn't be answered as you didn't know the answer."
        self.parameters = {
            "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The question that couldn't be answered"
                    },
                    "notes": {
                        "type": "string",
                        "description": "Any additional information about the conversation that's worth recording to give context"
                    }
                },
                "required": ["question"],
                "additionalProperties": False
            }


    def tool_definition(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        }

    def api_push_message(self, message: str):
        print(f"Pushing message: {message}")
        return f"Message '{message}' pushed"