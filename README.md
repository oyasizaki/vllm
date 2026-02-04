## Setting up `OS` (Local)
```bash
wsl --install Ubuntu-22.04
```



## Installing `uv`


Use curl to download the script and execute it with sh:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If your system doesn't have curl, you can use wget:
```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

Request a specific version by including it in the URL:
```bash
curl -LsSf https://astral.sh/uv/0.9.29/install.sh | sh
```


Run this command to add uv to your PATH for the current session:
```bash
source $HOME/.local/bin/env
```
Verify Installation
```bash
uv --version
```


## Installing `Dependencies` (Local)
Check GPU Memory First
```bash
nvidia-smi
```
Install C Compiler
```bash
sudo apt update
sudo apt install build-essential -y
```
Install C Compiler
```bash
sudo apt install python3.10-dev -y
```
## Installing `CUDA Toolkit` (Local)
Check GPU Memory First
```bash
wget https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda_12.6.0_560.28.03_linux.run
sudo sh cuda_12.6.0_560.28.03_linux.run
```
Set Environment Variables
```bash
echo 'export CUDA_HOME=/usr/local/cuda' >> ~/.bashrc
echo 'export PATH=$CUDA_HOME/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```
Verify Installation
```bash
nvcc --version
```
## Setting-up  `env` (Optional)
```bash
sudo apt install python3.10-venv
python3 -m venv ~/.venv_vllm
source ~/.venv_vllm/bin/activate
```
## Installing `vLLM`
```bash
uv pip install vllm
```
To activate your virtual environment in a new terminal:
```bash
source ~/.venv/bin/activate
```
## Login to Huggingface 
(for running restricted models)
```bash
huggingface-cli login
```
## Run vLLM
For getting started you can use (Don't expect good performance):
```bash
vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
  --host 0.0.0.0 \
  --port 8000 \
  --gpu-memory-utilization 0.75
```

If you have better GPU then you can run:
```bash
vllm serve meta-llama/Llama-3.2-3B-Instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --gpu-memory-utilization 0.75
```
I am using
```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --gpu-memory-utilization 0.75
```

## Connect with langflow
Flow
<img width="880" height="524" alt="image" src="https://github.com/user-attachments/assets/078ea966-7dde-4a58-967e-bf6780a89a06" />
Chatbox
<img width="829" height="524" alt="image" src="https://github.com/user-attachments/assets/f3f48c2c-b0b1-4a68-8be8-854e71d40d6a" />



 
