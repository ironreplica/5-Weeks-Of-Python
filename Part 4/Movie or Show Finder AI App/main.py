import requests
import openai

api_key = '504e2a2f610a4a1e97e3995a2e2d8e9a'

system_content = "Be a tv show or movie finder, be honest if the show is bad do not reccomend it."
user_content = input('Hello, give me a TV show or movie name and I will tell you if its worth a watch!\n')

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.aimlapi.com",
)

chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
    temperature=0.7,
    max_tokens=128,
)

response = chat_completion.choices[0].message.content
print("AI/ML API:\n", response)