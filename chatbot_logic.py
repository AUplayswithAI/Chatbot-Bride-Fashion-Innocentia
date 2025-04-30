import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def handle_customer_query(user_input):
    prompt = f"""
Du bist ein freundlicher Kundenberater für einen Brautkleidhersteller. Beantworte Kundenanfragen professionell, höflich und informativ.

Anfrage: "{user_input}"

Antwort:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=300
    )
    return response['choices'][0]['message']['content'].strip()
