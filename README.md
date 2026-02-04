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


## Installing `vLLM`

```bash
uv pip install vllm
```


 # vLLM Installation on Ubuntu / WSL (Correct Way)

This guide avoids PEP 668 errors and installs vLLM safely using a virtual environment.

---

## Step 1 — Install venv support (once)

```bash
sudo apt update
sudo apt install python3-venv python3-full -y
```

##Step 2 — Create clean virtual environment

```bash
cd ~/vllm
python3 -m venv .venv
```

##Step 3 — Activate it

```bash
source .venv/bin/activate
```

###Your prompt should look like:

```bash
(.venv) home@ANKAN:~/vllm$
```

##Step 4 — Install vLLM inside venv

```bash
pip install --upgrade pip
pip install vllm
```

##Step 5 — Run your program

```bash
python main.py
```
