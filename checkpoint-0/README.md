
# Checkpoint 0 — Hello, OpenAI 👋
**Time:** 10–20 min | **Goal:** Confirm your local setup can call the OpenAI API

---

## What you’re doing

You will:

1. Clone the repository
2. Create a Python virtual environment
3. Install dependencies from [`requirements.txt`](requirements.txt)
4. Add your `OPENAI_API_KEY` using a `.env` file
5. Run [`checkpoint-0/hello-openai.py`](checkpoint-0/hello-openai.py)

---

## Steps

### 1. Clone the repository

Use **either** HTTPS or SSH.

```bash
# HTTPS
git clone https://github.com/<org>/<repo>.git

# SSH
git clone git@github.com:<org>/<repo>.git
```

---

### 2. `cd` into the project`

From your terminal:

```bash
cd <repo>
```

---

### 3. Create and activate a virtual environment (`.venv`)

Create the environment **from the repository root** (`<repo>`), then activate it.

#### macOS / Linux

```bash
cd <repo>
python -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```powershell
cd <repo>
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 4. Upgrade pip and install dependencies

Install from the repository root so pip can find [`requirements.txt`](requirements.txt).

```bash
cd <repo>
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### 5. Complete the `.env` file with the shared workshop API key

This checkpoint loads environment variables via [`dotenv.load_dotenv()`](checkpoint-0/hello-openai.py:4).

Enter the file `.env` in the **repository root** (`<repo>/.env`) and view the environment variable `OPENAI_API_KEY`.

This API key is shared across the workshop, but is incomplete for security reasons. **Complete it with the characters provided by your instructor.**

```bash
OPENAI_API_KEY=sk-proj-<remaining_characters>
```

Do not commit your key.

---

### 6. Run the test script from the correct directory

Run from inside `checkpoint-0/`:

```bash
cd <repo>/checkpoint-0/
python hello-openai.py
```

Or run from the project root:

```bash
cd <repo>
python checkpoint-0/hello-openai.py

---

## What you’ll see (expected behavior)

If everything is configured correctly:

- The script sends a single prompt to an OpenAI chat model via LangChain.
- You will see **one short printed response** in your terminal.
- The exact text will vary, but a successful run prints a message and exits without errors.

---

## Troubleshooting

### You’re in the wrong directory

Symptoms: `python: can't open file ...` or the script cannot find your `.env`.

Fix:

```bash
pwd
ls
cd <repo>/checkpoint-0/
```

### Your virtual environment is not activated

Symptoms: `ModuleNotFoundError` for packages like `openai` or `langchain`.

Fix (macOS/Linux):

```bash
cd <repo>
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Fix (Windows PowerShell):

```powershell
cd <repo>
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Missing or invalid `OPENAI_API_KEY`

Symptoms: authentication errors from the OpenAI API.

Fix:

1. Confirm you created `<repo>/.env`
2. Ensure it contains:

```bash
OPENAI_API_KEY=your_key_goes_here
```

3. Re-run the script from [`checkpoint-0/`](checkpoint-0/README.md)

### Dependency install failures

Symptoms: pip errors during install.

Fix:

```bash
cd <repo>
python -m pip install --upgrade pip
python -m pip install -r requirements.txt --upgrade
```

If you still have issues, delete and recreate the venv:

```bash
cd <repo>
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
