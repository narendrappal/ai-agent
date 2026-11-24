from openai import OpenAI
from dotenv import load_dotenv
import os

# Load config from .env
load_dotenv()
print("BASE_URL:", repr(os.getenv("BASE_URL")))
print("MODEL:", repr(os.getenv("MODEL")))
# Create a client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# Sent the request to AI model
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content":"What is Artificial Intelligence?"
        }
    ]   
)

# Display the response
print(response.choices[0].message.content)