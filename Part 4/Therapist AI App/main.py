import requests
import openai

api_key = '504e2a2f610a4a1e97e3995a2e2d8e9a'

system_content = "Be my therapist, ask me how I am and talk to me about my problems, end every response with a question so I can have a conversation with you."
# user_content = input('How are you doing today?\n')

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
    print(chat_completion.choices[0].message.content)
    question(input('Reply: '))
question(input('How are you doing today?\n'))