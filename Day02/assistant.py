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
messages = []
while True:
    user_input=input("\nYou: ")
    if user_input.lower() == "quit":
        print("\n AI: Goodbye!")
        break
    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    result = response.choices[0].message.content
    print("\nAI: ",result)
    messages.append(
        {
            "role":"assistant",
            "content":result
        }
    )
    print("-" *40)
    print("         History")
    print("-" *40)
    for message in messages:
        print(message)
    print("-" *40)