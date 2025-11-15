"""
main.py

Takes command line args:
    url: uri to hosted model
    model: model name
    temperature: temperature (hyperparam) of model OPTIONAL, default 0.6
    max_tokens: number of maximum output tokens from model OPTIONAL, default 1024

Creates instance of llm_request class from llm_request.py, takes input from user for a prompt, uses llm_request to prompt the LLM hosted at the url, prints response and exits

Just an example of how you could use vllm, not limited to this

"""

from llm_request import llm_request
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to hosted model (via vllm)")
    parser.add_argument("model", help="model name")
    parser.add_argument("--temperature", help="temperature, default 0.6", default=.6)
    parser.add_argument("--max_tokens", help="max tokens, default 1024", default=1024)
    
    args = parser.parse_args()
    url = args.url
    model = args.model
    temperature = args.temperature
    max_tokens = args.max_tokens  

    model_request = llm_request(url, model, temperature, max_tokens) #instantiate
    prompt = input("Enter a test prompt: ") #get prompt from user

    ans = model_request.run(prompt) #send request, receive response, get answer

    print(ans)




if __name__=="__main__":
    main()
