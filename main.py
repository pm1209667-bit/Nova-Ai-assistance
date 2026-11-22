import os
from pathlib import Path
from datetime import datetime
from typing import List, Optional

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="NOVA AI Assistant", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE_DIR / "static" / "index.html").read_text(encoding="utf-8")

def local_reply(message: str) -> str:
    q = message.lower().strip()
    now = datetime.now()
    if any(x in q for x in ["hello", "hi", "hey", "namaste"]):
        return "Hello! I'm NOVA, your personal AI assistant. What can I help you with?"
    if "time" in q:
        return f"The current server time is {now.strftime('%I:%M %p')}."
    if "date" in q or "today" in q:
        return f"Today is {now.strftime('%A, %d %B %Y')}."
    if "your name" in q or "who are you" in q:
        return "I'm NOVA, your personal voice assistant project."
    if "help" in q:
        return "You can ask me questions, use the microphone, or try asking for the time and date. Add an AI API key in the backend environment to enable open-ended AI answers."
    return ("I'm running in starter mode, so I can handle a few basic requests. "
            "To answer open-ended questions, configure an AI provider in the backend. "
            "Your message was received: " + message)

async def ai_reply(message: str, history: List[ChatMessage]) -> str:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        return local_reply(message)
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        messages = [{"role": "system", "content": (
            "You are NOVA, a helpful, concise personal voice assistant. "
            "Use clear beginner-friendly language. If the user speaks Hindi, reply in Hindi; "
            "if English, reply in English. Do not claim to perform actions you cannot perform."
        )}]
        for item in (history or [])[-10:]:
            if item.role in ("user", "assistant"):
                messages.append({"role": item.role, "content": item.content[:4000]})
        messages.append({"role": "user", "content": message[:4000]})
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)
        return response.choices[0].message.content or "I couldn't generate a response just now."
    except Exception as exc:
        print("AI provider error:", repr(exc))
        return "I couldn't reach the AI service. Check the backend API key, model name, and internet connection."

@app.post("/api/chat")
async def chat(payload: ChatRequest):
    message = payload.message.strip()
    if not message:
        return {"reply": "Please type or say something first.", "mode": "demo"}
    reply = await ai_reply(message, payload.history or [])
    mode = "ai" if os.getenv("OPENAI_API_KEY", "").strip() else "demo"
    return {"reply": reply, "mode": mode}

@app.get("/api/health")
def health():
    return {"status": "ok", "assistant": "NOVA", "ai_configured": bool(os.getenv("OPENAI_API_KEY", "").strip())}
