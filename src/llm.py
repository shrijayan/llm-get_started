import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
load_dotenv()

with open('config.json') as f:
    config = json.load(f)

with open('system_prompt.txt', 'r') as f:
    system_prompt = f.read()

class LLM:
    def __init__(self):
        self.model_name = config['AZURE_OPENAI_MODEL_NAME']
    
    def generate_completion(self, user_prompt):
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        response = client.chat.completions.create(
            model=self.model_name, 
            messages=[{"role": "system", "content": system_prompt},
                      {"role": "user", "content": user_prompt}],
        )
        return response.choices[0].message.content