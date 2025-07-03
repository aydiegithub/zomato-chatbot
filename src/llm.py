from dotenv import load_dotenv
import os
# import openai
from src.prompt import system_instruction
import requests

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API")

API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(user_message):
    messages.append({"role": "user", "content": user_message})

    # Limit to last 4 interactions to prevent token overflow
    trimmed_messages = [messages[0]] + messages[-6:]  # keep system + last 3 Q&A

    payload = {
        "model": "llama3-8b-8192",
        "messages": trimmed_messages,
        "temperature": 0.7,
        "max_tokens": 300
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return "❌ API Error"

    reply = response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply








"""
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


messages = [
    {"role": "system", "content": system_instruction}
]


def ask_order(user_message):
    messages.append({"role": "user", "content": user_message})

    # Formating the prompt
    prompt = ""
    for msg in messages:
        role = msg['role']
        content = msg['content']
        if role == 'system':
            prompt += f"<|system|>\n{content}\n"
        elif role == "user":
            prompt += f"<|user|>\n{content}\n"
        elif role == 'assistant':
            prompt += f"<|assistant|>\n{content}\n"

    payload = {
        "inputs": prompt + "<|assistant|>\n",
        "parameters": {
            "temperature": 0.7, "max_new_tokens": 256
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json = payload)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    result = response.json()
    output_text = result[0]["generated_text"].split("<|assistant|>\n")[-1].strip()

    messages.append({"role": "assistant", "content": output_text})
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    return output_text

"""







"""
# Below code snipped is for OpenAI APIs

# openai.api_key = os.getenv("OPENAI_API_KEY")
# print("Loaded API key:", openai.api_key[:8])

def ask_order(message, model="gpt-3.5-turbo", temperature=0):
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    print("OpenAI response:", response)
    return response.choices[0].message.content
"""
