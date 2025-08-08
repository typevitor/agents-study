from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests

class PusherToolInput(BaseModel):
    """A message to be set to the user."""
    message: str = Field(..., description="Message to be sent to the user.")

class PusherNotificationTool(BaseTool):
    name: str = "Send a push notification"
    description: str = (
        "A tool for sending push messages to users."
    )
    args_schema: Type[BaseModel] = PusherToolInput

    def _run(self, message: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")
        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Push: {message}")
        payload = {"user": pushover_user, "token": pushover_token, "message": message}
        requests.post(pushover_url, data=payload)
        return '{"notification": "ok"}'
