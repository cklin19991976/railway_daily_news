# =========================
# app/digest.py
# =========================
from datetime import datetime
from zoneinfo import ZoneInfo
from app.config import APP_NAME, TIMEZONE, WATCHLIST
from app.news import get_all_news
from app.market import get_market_snapshot
from app.ai_summary import build_fallback_summary
from app.templates import build_email_html
from app.emailer import send_email


def build_digest():
    news = get_all_news()
    market = get_market_snapshot(WATCHLIST)
    summary = build_fallback_summary(news, market)
    html = build_email_html(news, market, summary)
    subject = f"{APP_NAME} - {datetime.now(ZoneInfo(TIMEZONE)).strftime('%Y-%m-%d')}"
    return subject, html


def send_digest():
    subject, html = build_digest()
    send_email(subject, html)
    return subject