import os
from openai import api_key
import requests


api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key=os.getenv("OPENAI_API_KEY") 
request_headers = {"Content-Type: application/json", "Authorization: Bearer" + api_key}

request_data{"model":}

requests.post(api_endpoint,headers=request_headers, json{})


