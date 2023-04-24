import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Welcome to our education-based chatbot! We are delighted to have you here. As an AI-powered virtual assistant, we are committed to helping you on your educational journey. "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "EDUARIOT")

demo.launch()