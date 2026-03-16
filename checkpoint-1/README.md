# Checkpoint 1 — Giving Jarvis a Brain 🧠
**Time:** 20–40 min | **Goal:** Make Jarvis answer questions using a real LLM

---

## What's happening under the hood?

When you type a message and hit Enter, here's what occurs:

1. Your text gets **tokenized** — broken into chunks the model understands
2. Those tokens are sent over HTTP to Google's servers
3. A **transformer model** runs a forward pass and predicts the best reply
4. The response tokens are decoded back into text and returned to you

This is called an **LLM wrapper** — your code is a thin layer around a 
powerful model you don't have to train yourself.

---

## Steps

### 1. Paste your API key
Open `jarvis_llm.py` and replace `"YOUR_KEY_HERE"` with the key you got 
from [aistudio.google.com](https://aistudio.google.com).

### 2. Run the starter file
\```bash
cd checkpoint-1
python jarvis_llm.py
\```

You should see `You:` — type anything and Jarvis will reply.

### 3. Complete the TODOs in the file
There are 3 small TODOs marked in the code. Fill them in one at a time.

### 4. Try these prompts to test it
- `Explain neural networks like I'm 10`
- `What is a transformer model?`
- `Quiz me on machine learning basics`
- `Summarize: gradient descent is an optimization algorithm that...`

---

## Challenge tasks (if you finish early)
- [ ] Add a **system prompt** that gives Jarvis a personality
- [ ] Keep a **conversation history** so Jarvis remembers earlier messages
- [ ] Print the response **word by word** with a small delay (streaming feel)

---

## Common errors

| Error | Fix |
|---|---|
| `API_KEY_INVALID` | Double-check you copied the full key |
| `ModuleNotFoundError` | Run `pip install google-generativeai` |
| `quota exceeded` | Switch to the Groq fallback below |

---

## Fallback: Groq (if Gemini quota runs out)
\```python
# pip install groq
from groq import Groq
client = Groq(api_key="YOUR_GROQ_KEY")  # free at console.groq.com

def ask_jarvis(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
\```