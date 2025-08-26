import gradio as gr
from dotenv import load_dotenv
from agents import Runner, trace, gen_trace_id
from custom_agents.game_recomender_agent import manager_agent

load_dotenv(override=True)

trace_id=gen_trace_id()

async def run_chat(user_message: str, chat_history: list):
    chat_history.append({"role": "user", "content": user_message})
    chat_history.append({"role": "assistant", "content": "Pensando..."})
    yield chat_history, ""

    messages = [{"role": message["role"], "content": message["content"]} for message in chat_history[:-1]]
    
    with trace("Agente de Recomendação de Jogos", trace_id=trace_id):
        print(f"Running Manager Agent with messages: {messages}")
        result = await Runner.run(
            manager_agent,
            messages
        )
    chat_history[-1] = {"role": "assistant", "content": result.final_output}
    yield chat_history, ""

def reset_conversation():
    """Função para resetar a conversa e criar um novo trace"""
    global trace_id
    trace_id = gen_trace_id()
    return [], []


with gr.Blocks() as ui:
    chat = gr.Chatbot(type="messages", label="Agente de Recomendação de Jogos")
    chat_history = gr.State([])
    txt = gr.Textbox(placeholder="Escreva aqui...", show_label=False)
    btn = gr.Button("Enviar")
    reset_btn = gr.Button("Resetar Conversa")
    
    btn.click(
        fn=run_chat,
        inputs=[txt, chat_history],
        outputs=[chat, txt],
    )
    txt.submit(
        fn=run_chat,
        inputs=[txt, chat_history],
        outputs=[chat, txt],
    )

    reset_btn.click(
        fn=reset_conversation,
        outputs=[chat, chat_history]
    )

ui.launch(inbrowser=True)