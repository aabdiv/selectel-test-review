from typing import Awaitable, Callable

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.config import settings


def create_scheduler(job: Callable[[], Awaitable[None]]) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        job,
        trigger="interval",
        minutes=settings.parse_schedule_minutes,    # wrong parameter name, must be minutes https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job
        coalesce=True,
        max_instances=1,
    )
    return scheduler
