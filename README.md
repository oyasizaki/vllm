## Installing `uv`

You can install **uv** using the standalone installer or via your preferred package manager.

---

### Standalone Installer

`uv` provides a standalone installer script for quick setup.

#### Use irm to download the script and execute it with iex

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
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
