# =========================
# app/config.py
# =========================
import os
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
EMAIL_FROM = os.getenv("EMAIL_FROM", SMTP_USER)
EMAIL_TO = os.getenv("EMAIL_TO", SMTP_USER)
TIMEZONE = os.getenv("TIMEZONE", "Europe/Dublin")
SEND_HOUR = int(os.getenv("SEND_HOUR", "7"))
SEND_MINUTE = int(os.getenv("SEND_MINUTE", "0"))
APP_NAME = os.getenv("APP_NAME", "Daily Market Brief")
WATCHLIST = [x.strip() for x in os.getenv("WATCHLIST", "NVDA,AAPL,TSLA,SPY,QQQ,TSM,MSFT,ASML,META,GOOG,2330.TW,0050.TW,0056.TW,1215.TW").split(",") if x.strip()]
ENABLE_AI_SUMMARY = os.getenv("ENABLE_AI_SUMMARY", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")