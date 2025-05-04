from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyDN9-S8D47jyYY3tnRwnyGx8yiwXuGgGFw"

def hello():
    response = completion(
        model="gemini/gemini-2.0-flash-exp", 
        messages=[{"role": "user", "content": "who is the president of the united states?"}]
    )
    print(f"\n\n **response** \n\n")
    print(response['choices'][0]['message']['content'])
