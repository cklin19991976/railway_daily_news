# =========================
# app/worker.py
# =========================
import time
from zoneinfo import ZoneInfo
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from app.config import SEND_HOUR, SEND_MINUTE, TIMEZONE
from app.digest import send_digest


def run_job():
    subject = send_digest()
    print(f"Digest sent: {subject}")


if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone=ZoneInfo(TIMEZONE))
    scheduler.add_job(
        run_job,
        CronTrigger(hour=SEND_HOUR, minute=SEND_MINUTE, timezone=ZoneInfo(TIMEZONE)),
        id="daily_digest",
        replace_existing=True,
    )
    print(f"Worker started. Scheduled for {SEND_HOUR:02d}:{SEND_MINUTE:02d} {TIMEZONE}")
    scheduler.start()