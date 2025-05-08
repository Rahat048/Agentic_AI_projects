from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.0-flash-exp:free"

import requests
import json

response = requests.post(
  url=f"https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {api_key}",
  },
  data=json.dumps({
    "model": MODEL,
    "messages": [
      {
        "role": "user",
        "content": "write a poem of 5 lines on rain in punjabi"
      }
    ]
  })
)


data = response.json()


print(data['choices'][0]['message']['content'])