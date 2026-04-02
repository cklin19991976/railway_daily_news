# =========================
# README.md
# =========================
# Railway Daily Market Brief (Bilingual EN + 繁中)
#
# Your selected watchlist:
# NVDA, AAPL, TSLA, SPY, QQQ, TSM, MSFT, ASML, META, GOOG,
# 2330.TW, 0050.TW, 0056.TW, 1215.TW
#
# Schedule:
# 07:00 every day, Ireland time (Europe/Dublin)
#
# Email target:
# your Gmail inbox
#
# Deployment steps:
# 1. Push to GitHub
# 2. In Railway, create project
# 3. Add TWO services from same repo:
#    - web    -> use Procfile.web
#    - worker -> use Procfile.worker
# 4. Add all environment variables from .env.example
# 5. Deploy
#
# Test endpoints:
# - /preview
# - /send-now
#
# Gmail setup:
# - Turn on Google 2-Step Verification
# - Create Gmail App Password
# - Put App Password in SMTP_PASSWORD
#
# Best future upgrades:
# - Add article ranking / de-duplication
# - Add Taiwan + US macro event calendar
# - Add AI explanation of why each item matters
# - Add “only send when important” mode
