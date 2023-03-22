import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')
openai.api_key=os.getenv('OPENAI_API_KEY')

def sendPrompt(prompt, session_messages):
    session_messages.append({"role": "user", "content":prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=session_messages
    )
    message = response.choices[0].message.content
    session_messages.append({"role": "assistant", "content":message})
    return message