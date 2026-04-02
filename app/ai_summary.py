# =========================
# app/ai_summary.py
# =========================
from app.config import ENABLE_AI_SUMMARY


def build_fallback_summary(news, market):
    us = news.get("us_stock", [])[:2]
    tw = news.get("tw_stock", [])[:2]
    lines_en = [
        "Today’s focus is on the biggest US and Taiwan market-moving headlines, plus your watchlist performance.",
        "Watch whether macro headlines, semiconductors, and ETF flows are driving the market tone.",
    ]
    lines_zh = [
        "今日重點整理美股與台股最可能影響市場的新聞，以及你的自選股表現。",
        "請特別留意總經、半導體與 ETF 資金流是否主導今日盤勢。",
    ]
    return {
        "en": " ".join(lines_en),
        "zh": " ".join(lines_zh),
    }