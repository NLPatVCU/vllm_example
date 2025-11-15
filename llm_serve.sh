#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --mem=100G
#SBATCH --cpus-per-task=16
#SBATCH --output=llm_serve_output.log
#SBATCH --job-name=llm_serve

# These commands serve the llm. In this case, I'm using the model I want, but
# you can use anything you want for this (within reason)
module load python/3.11

source .venv/bin/activate

vllm serve Qwen/Qwen3-30B-A3B-Instruct-2507 --max-model-len 10000 #consider changing max model len
