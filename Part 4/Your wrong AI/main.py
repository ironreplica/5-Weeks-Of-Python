import requests
import openai

api_key = '504e2a2f610a4a1e97e3995a2e2d8e9a'

system_content = "No matter what I say tell me I am wrong, and tell me its because {something completely irrelevant}. Do not furthur ellaborate or explain that it is a joke. Be harsh."
def question(user_input):
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.aimlapi.com",
    )

    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_input},
        ],
        temperature=0.7,
        max_tokens=128,
    )
    print(f'AI: {chat_completion.choices[0].message.content}')
    question(input('You: '))
question(input('I am an AI that knows more than you. Tell me something and I will tell you you are wrong.\n'))
