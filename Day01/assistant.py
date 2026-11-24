from openai import OpenAI
from dotenv import load_dotenv
import os

# Load config from .env
load_dotenv()
# Create a client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" *40)
print("         My Assistant")
print("=" *40)

while True:
    user_input=input("\nYou: ")
    if user_input.lower() == "quit":
        print("\n AI: Goodbye!")
        break
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":user_input
            }
        ]
    )
    print("\nAI: ",response.choices[0].message.content)