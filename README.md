# What is this?
This is a demo of how to use vllm to serve LLMs. This means you are sending requests with your prompt to an LLM which you host on your system. 

# How do I start
## Prerequisites
0. ```module load python/3.11```
1. Install uv ```curl -LsSf https://astral.sh/uv/install.sh | sh```
2. Create virtualenv ```uv venv --python 3.11 --seed```
3. Activate virtualenv ```source .venv/bin/activate```
4. Install requests ```uv pip install requests```
5. Install necessary components ```export UV_HTTP_TIMEOUT=600 #just in case``` ```uv pip install vllm --torch-backend=auto```

## Serving and Requesting
0. Serve your desired language model. If you're on athena, you can use the llm_serve.sh SBATCH script. ```sbatch llm_serve.sh``` and just change Qwen/Qwen3-30B-A3B-Instruct-2507 to your preferred LLM. Pay attention to the output. It should say "Application Startup Complete." when it is ready to prompt. Also important to pay attention to is the node and port it is hosted on, this will be printed in the log. On athena, pay attention to what node your llm_serve job is running on. Your uri (if on athena or some cluster) is "http://node:8000/v1/completions", where node is something like athena534 for example. If running on a regular server or locally, "http://localhost:8000/v1/completions"
1. Now you can prompt. run ```python main.py <uri> <model>``` where uri is your uri as mentioned in step one, and model is what you changed Qwen/Qwen3-30B-A3B-Instruct-2507 to in step one
2. It will ask you to input a prompt, input your prompt
3. Behold, an answer from the LLM!

## Other Notes
- There are a LOT of other parameters you can use with vllm other than temp and max tokens. See link in comment of llm_request.py
- This is a basic implementation but you can do much more with vllm, highly recommend checking documentation
- Remember to cancel serve jobs when you aren't using them!!! I will not be responsible for this
- multi-GPU inference might be a thing, not sure. would make things fassst
- when in doubt with main.py cli, ```python main.py -h``` should help
  
For questions, comments, or suggestions email me at ndil@vcu.edu

Happy coding!

