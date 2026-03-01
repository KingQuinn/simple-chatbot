from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    if not TOKEN:
        return "Error: OPENAI_API_KEY not found in environment variables or .env file."
    
    client = OpenAI(api_key=TOKEN)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Act as an insightful yet friendly AI researcher named Lisa"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with OpenAI: {e}"

if __name__ == "__main__":
    print("Lisa: Hello! I'm Lisa, an AI researcher. Type 'end', 'bye', or 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
            
        if user_input.lower() in ["end", "bye", "quit"]:
            print("Lisa: Goodbye! It was a pleasure chatting.")
            break

        response = get_response(user_input)
        print("Lisa:", response)
