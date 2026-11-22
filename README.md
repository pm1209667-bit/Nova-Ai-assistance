# NOVA AI — Personal Voice Assistant

NOVA is a beginner-friendly voice-enabled AI assistant website built with **Python, FastAPI, HTML, CSS and JavaScript**.

## Features

- Dark futuristic responsive web interface
- Browser microphone input (Web Speech API)
- Spoken assistant replies (Speech Synthesis)
- Text chat
- Python/FastAPI backend
- Demo mode works without an AI API key
- Optional AI responses through an OpenAI API key
- Conversation context sent with recent messages
- Health endpoint to check backend status

## Project structure

```text
nova-ai-assistant/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

## Run locally (Windows)

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the VS Code terminal and run:

```bash
python -m venv .venv
```

5. Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

6. Install dependencies:

```bash
pip install -r requirements.txt
```

7. Start the server:

```bash
uvicorn main:app --reload
```

8. Open `http://127.0.0.1:8000` in Google Chrome and allow microphone access.

## Enable AI answers (optional)

The project runs in demo mode without a paid service key. To enable AI answers:

1. Create your own API key with an AI provider that supports the OpenAI Python SDK.
2. Copy `.env.example` to a new file named `.env`.
3. Put your secret key in `.env`:

```env
OPENAI_API_KEY=your_secret_key_here
OPENAI_MODEL=gpt-4o-mini
```

4. Stop and restart the server.

**Important:** API access may cost money and is not guaranteed to be free. Check your provider's current pricing and usage limits. Never put API keys in `static/app.js`, HTML, or a public GitHub repository. Never commit `.env`.

## GitHub upload

Create a new empty repository on GitHub, for example `nova-ai-assistant`.

Then run these commands from this project folder:

```bash
git init
git add .
git commit -m "Build NOVA voice AI assistant"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/nova-ai-assistant.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not upload `.env`.

## Deploying online

GitHub stores your source code; it does not run the Python backend by itself. Deploy the FastAPI app to a Python-compatible hosting service and configure `OPENAI_API_KEY` as a private environment variable in that service if you enable AI mode. Free hosting availability, sleep limits, and pricing can change.

For a basic deployment, use the start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

If your hosting provider requires a fixed port, follow its platform instructions.

## Browser notes

- Voice recognition support varies by browser and device. Google Chrome is recommended for initial testing.
- Microphone permission is required.
- Browsers generally require a secure context (HTTPS) or localhost for microphone access.
- Speech recognition may use browser/vendor services; do not assume audio stays entirely on-device.
- Spoken responses use the browser's speech synthesis voices, which vary by device.

## Current limitations

- This is a starter personal assistant, not a fully autonomous agent.
- Demo mode only handles a small number of simple requests.
- The optional AI integration sends the current message and recent chat context to the configured AI provider.
- It does not access private files, email, or other apps unless you deliberately add and authorize those integrations.
- Do not use it for emergency services or high-stakes decisions.

## Next improvements

- Add a user-controlled persistent chat history
- Add PDF/CSV/Excel analysis tools
- Add configurable Hindi/English voice selection
- Add authentication and rate limiting before public deployment
- Add explicit permission checks before any computer or account actions
