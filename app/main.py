from __future__ import annotations

import asyncio
import sys
from pathlib import Path

if __package__ in {None, ""}:
    # Support running this file directly (python app/main.py) in IDEs.
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from aiogram import Bot, Dispatcher

from app.config import load_config
from app.db.connection import Db
from app.db.schema import init_db
from app.logging_config import setup_logging
from app.middlewares.admin_only import AdminOnlyMiddleware
from app.routers.start import router as start_router


async def run() -> None:
    setup_logging()
    cfg = load_config()

    await init_db(Db(cfg.db_path))

    bot = Bot(token=cfg.bot_token)
    dp = Dispatcher()

    dp.message.middleware(AdminOnlyMiddleware(cfg.admin_ids))
    dp.callback_query.middleware(AdminOnlyMiddleware(cfg.admin_ids))

    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run())