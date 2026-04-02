# =========================
# app/main.py
# =========================
from fastapi import FastAPI, Response
from app.digest import build_digest, send_digest
from app.config import APP_NAME

app = FastAPI(title=APP_NAME)


@app.get("/")
def home():
    return {"status": "ok", "service": APP_NAME}


@app.get("/send-now")
def send_now():
    subject = send_digest()
    return {"status": "sent", "subject": subject}


@app.get("/preview", response_class=Response)
def preview():
    _, html = build_digest()
    return Response(content=html, media_type="text/html")