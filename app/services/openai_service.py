import openai
import os

openai.api_key=os.getenv("OPENAI_API_KEY")

def generate_resume_summary(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"You are a resume assistant."},
            {"role":"user", "content":user_input}
        ]
    )
    return response['choices'][0]['message']['content']