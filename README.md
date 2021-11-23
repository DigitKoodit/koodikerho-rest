# Koodikerho REST

### Requirements

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads) (>=3.9)
- [Insomnia](https://insomnia.rest/download) (REST client, recommended for testing the API)

### Setup

1. **Clone this repo:**

```
git clone git@github.com:DigitKoodit/koodikerho-rest.git
```
OR
```
git clone https://github.com/DigitKoodit/koodikerho-rest.git
```

2. **Navigate to the directory you cloned:**

```
cd koodikerho-rest
```

3. **Create a Python virtual environment:**

(Use `python` or `python3` command depending on your system)
```
python -m venv venv
```

4. **Activate the virtual env:**

macOS, Linux, WSL, Git Bash:
```
source venv/bin/activate
```

Windows cmd.exe:
```
venv\Scripts\activate.bat
```

Windows PowerShell:
```
venv\Scripts\Activate.ps1
```

5. **Install the PyPI packages:**
```
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt -r requirements-dev.txt
```

### Running

```
uvicorn main:app --reload
```
