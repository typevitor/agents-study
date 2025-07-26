from dotenv import load_dotenv
from openai_provider import OpenAIProvider
from file_reader import FileReader
import gradio as gr
from chat import Chat

load_dotenv(override=True)

name = "Vitor Leal"

reader = FileReader("curriculum_agent/data/me.pdf");
curriculum_text = reader.read_pdf();
with open("curriculum_agent/data/summary.txt", "r", encoding="utf-8") as filesummary:
    summary = filesummary.read()

chatController = Chat(name, curriculum_text, summary)

gr.ChatInterface(chatController.chat, type="messages").launch()