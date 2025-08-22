from dotenv import load_dotenv
import gradio as gr
from application.file_reader import FileReader
from application.chat import Chat

load_dotenv(override=True)

name = "Vitor Leal"
with open("data/summary.txt", "r", encoding="utf-8") as filesummary:
    summary = filesummary.read()

chatController = Chat(name, summary)

gr.ChatInterface(chatController.chat, type="messages").launch()