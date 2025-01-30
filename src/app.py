import gradio as gr
from src.chat.chatbot import ChatBot

chatbot = ChatBot()

def chat(message, history):
    response = chatbot.chat(message, history)
    return response

gr.ChatInterface(fn=chat, type="messages").launch(pwa=True)