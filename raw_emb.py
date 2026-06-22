
import os
import tempfile
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)   

#print(conversation.choices[0].message.content)

response = client.embeddings.create(input = " Your Text string goes here", model = "text-embedding-3-small")

print(response)
print(response.data[0].embedding)