import gradio as gr
import asyncio

def slow_response(name):
    #await asyncio.sleep(2)
    return f"Hello, {name}! (after waiting)"

gr.Interface(fn=slow_response, inputs="text", outputs="text").launch()
