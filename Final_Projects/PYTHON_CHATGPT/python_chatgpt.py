from openai import api_key
import requests


api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = os.getenv("OPENAI_API_KEY")
