"""
llm_request.py

has llm_request_class, a wrapper for making HTTP requests to vllm endpoint
url: endpoint uri
model: model name
temperature: model temperature (hyperparameter)
max_tokens: Number of allowed output tokens in response

"""

import html
import requests

class llm_request:
    def __init__(self, url, model, temperature, max_tokens):
        self.url = url
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
    def run(self,prompt):

        headers={"Content-Type": "application/json"}
        data = {
            "model":self.model,
            "prompt":prompt,
            "temperature":self.temperature,
            "max_tokens":self.max_tokens
            # all possible request body params here: https://platform.openai.com/docs/api-reference/chat/create
        }#body of request
        response = requests.post(self.url, headers=headers,json=data, verify=False)#make request
        #print(response.json())
        assistant_message = response.json()['choices'][0]['text']#extract response
        return assistant_message
