# Checkpoint 1 — Giving Jarvis a Brain 🧠
**Time:** 20–40 min | **Goal:** Make Jarvis answer questions using a real LLM

---

## What's happening under the hood?

When you type a message and hit Enter, here's what occurs:

1. Your text gets **tokenized** — broken into chunks the model understands
2. A **transformer model** runs a forward pass and predicts the best reply
3. The response tokens are decoded back into text and returned to you

This is called an **LLM wrapper** — your code is a thin layer around a 
powerful model you don't have to train yourself.

---

## Steps

### 1. Paste your API key
Open `jarvis_llm.py` and replace `"YOUR_KEY_HERE"` with the key you got 
from the slides.

### 2. Run the starter file
\```bash
cd checkpoint-1
python jarvis_llm.py
\```


Fill out here Oliver