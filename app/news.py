# =========================
# app/news.py
# =========================
import requests
from app.config import NEWSAPI_KEY

NEWS_API_URL = "https://newsapi.org/v2/everything"
TOP_HEADLINES_URL = "https://newsapi.org/v2/top-headlines"


def _request(url: str, params: dict):
    headers = {"X-Api-Key": NEWSAPI_KEY}
    r = requests.get(url, params=params, headers=headers, timeout=25)
    r.raise_for_status()
    data = r.json()
    return data.get("articles", [])


def simplify_articles(articles, limit=6):
    out = []
    seen = set()
    for a in articles:
        title = (a.get("title") or "").strip()
        url = a.get("url") or ""
        source = (a.get("source") or {}).get("name", "Unknown")
        desc = (a.get("description") or "").strip()
        if not title or not url:
            continue
        key = title.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append({
            "title": title,
            "url": url,
            "source": source,
            "description": desc,
        })
        if len(out) >= limit:
            break
    return out


def get_us_general_news(limit=5):
    articles = _request(TOP_HEADLINES_URL, {"country": "us", "pageSize": 20})
    return simplify_articles(articles, limit)


def get_taiwan_general_news(limit=5):
    articles = _request(NEWS_API_URL, {
        "q": 'Taiwan OR 台灣 OR 台灣新聞 OR Taipei OR TSMC',
        "sortBy": "publishedAt",
        "pageSize": 20,
    })
    return simplify_articles(articles, limit)


def get_us_stock_news(limit=5):
    articles = _request(NEWS_API_URL, {
        "q": 'US stock market OR Wall Street OR S&P 500 OR Nasdaq OR Fed OR inflation',
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
    })
    return simplify_articles(articles, limit)


def get_taiwan_stock_news(limit=5):
    articles = _request(NEWS_API_URL, {
        "q": '台股 OR Taiwan stock market OR 加權指數 OR 台積電 OR ETF OR 證交所',
        "sortBy": "publishedAt",
        "pageSize": 20,
    })
    return simplify_articles(articles, limit)


def get_all_news():
    return {
        "us_general": get_us_general_news(),
        "tw_general": get_taiwan_general_news(),
        "us_stock": get_us_stock_news(),
        "tw_stock": get_taiwan_stock_news(),
    }
