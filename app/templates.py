# =========================
# app/templates.py
# =========================
from datetime import datetime
from zoneinfo import ZoneInfo
from app.config import TIMEZONE, APP_NAME
from app.market import fmt_num, fmt_pct


def render_news_section(title_en, title_zh, items):
    if not items:
        return f"<h2>{title_en} / {title_zh}</h2><p>No major items found today / 今日未抓到明顯重點新聞</p>"
    html = f"<h2>{title_en} / {title_zh}</h2><ul>"
    for item in items:
        html += f"""
        <li style='margin-bottom:14px;'>
          <a href='{item['url']}' style='font-weight:bold;font-size:16px;text-decoration:none;'>{item['title']}</a><br/>
          <span style='color:#666;'>{item['source']}</span><br/>
          <span>{item['description'] or ''}</span>
        </li>
        """
    html += "</ul>"
    return html


def render_market_table(title_en, title_zh, rows):
    tr = ""
    for r in rows:
        tr += f"<tr><td style='padding:8px;border:1px solid #ddd;'>{r.get('label', r['ticker'])}</td><td style='padding:8px;border:1px solid #ddd;'>{fmt_num(r['price'])}</td><td style='padding:8px;border:1px solid #ddd;'>{fmt_pct(r['change_pct'])}</td></tr>"
    return f"""
    <h2>{title_en} / {title_zh}</h2>
    <table style='border-collapse:collapse;width:100%;margin-bottom:16px;'>
      <tr><th style='padding:8px;border:1px solid #ddd;'>Ticker</th><th style='padding:8px;border:1px solid #ddd;'>Price</th><th style='padding:8px;border:1px solid #ddd;'>Change</th></tr>
      {tr}
    </table>
    """


def build_email_html(news, market, summary):
    now = datetime.now(ZoneInfo(TIMEZONE)).strftime("%Y-%m-%d %H:%M")
    return f"""
    <html>
    <body style='font-family:Arial,sans-serif;line-height:1.6;color:#222;max-width:900px;margin:auto;'>
      <h1>{APP_NAME}</h1>
      <p><strong>Date:</strong> {now} ({TIMEZONE})</p>
      <p><strong>English:</strong> Your daily US + Taiwan news and market briefing.</p>
      <p><strong>繁體中文：</strong> 你的美股 + 台股每日新聞與市場摘要。</p>
      <hr/>
      <h2>What Matters Today / 今日重點</h2>
      <p><strong>EN:</strong> {summary['en']}</p>
      <p><strong>中文:</strong> {summary['zh']}</p>
      <hr/>
      {render_market_table('Major Indexes', '主要指數', market['indexes'])}
      {render_market_table('Your Watchlist', '你的自選股', market['watchlist'])}
      <hr/>
      {render_news_section('US Top News', '美國重要新聞', news['us_general'])}
      <hr/>
      {render_news_section('Taiwan Top News', '台灣重要新聞', news['tw_general'])}
      <hr/>
      {render_news_section('US Stock Market News', '美股市場新聞', news['us_stock'])}
      <hr/>
      {render_news_section('Taiwan Stock Market News', '台股市場新聞', news['tw_stock'])}
      <hr/>
      <p style='font-size:12px;color:#777;'>Generated automatically by Railway.</p>
    </body>
    </html>
    """