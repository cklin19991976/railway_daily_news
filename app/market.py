# =========================
# app/market.py
# =========================
import yfinance as yf

INDEXES = {
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "Dow": "^DJI",
    "VIX": "^VIX",
    "TAIEX": "^TWII",
}


def fmt_num(x):
    if x is None:
        return "N/A"
    try:
        return f"{x:,.2f}"
    except Exception:
        return str(x)


def fmt_pct(x):
    if x is None:
        return "N/A"
    try:
        return f"{x:+.2f}%"
    except Exception:
        return str(x)


def get_quote(ticker: str):
    try:
        t = yf.Ticker(ticker)
        info = t.fast_info
        price = info.get("lastPrice")
        prev = info.get("previousClose")
        if price is None or prev in (None, 0):
            hist = t.history(period="5d")
            if len(hist) >= 2:
                price = float(hist["Close"].iloc[-1])
                prev = float(hist["Close"].iloc[-2])
        chg = None if price is None or prev in (None, 0) else ((price - prev) / prev * 100)
        return {
            "ticker": ticker,
            "name": ticker,
            "price": price,
            "change_pct": chg,
        }
    except Exception:
        return {"ticker": ticker, "name": ticker, "price": None, "change_pct": None}


def get_market_snapshot(watchlist):
    indexes = [{"label": k, **get_quote(v)} for k, v in INDEXES.items()]
    watch = [get_quote(t) for t in watchlist]
    return {"indexes": indexes, "watchlist": watch}
