import os
from openai import OpenAI

# Initialize the client with your API key
# Make sure OPENAI_API_KEY is set in your environment variables use long api-key env var not working
client = OpenAI(api_key="")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
    model="gpt-4o-mini",  # "gpt-4o-mini" is not a valid model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."},
    ],
)

# Access the content of the message directly
print(completion.choices[0].message.content)
"""Printing the response:

Added .content to properly access the message content
The original code would print the entire message object
API Key:

Make sure you have set your OpenAI API key as an environment variable named OPENAI_API_KEY
Alternatively, you can pass it directly: client = OpenAI(api_key="your-api-key")"
"""
