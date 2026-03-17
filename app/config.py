from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    bot_token: str
    admin_ids: frozenset[int]
    db_path: str


def _parse_admin_ids(raw: str) -> frozenset[int]:
    ids: set[int] = set()
    for part in (raw or "").split(","):
        part = part.strip()
        if part:
            ids.add(int(part))
    return frozenset(ids)


def load_config() -> AppConfig:
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN", "").strip()
    if not bot_token or bot_token.upper() == "PUT_YOUR_TOKEN_HERE":
        raise RuntimeError(
            "Set a real BOT_TOKEN in .env (the default placeholder is not valid)."
        )

    return AppConfig(
        bot_token=bot_token,
        admin_ids=_parse_admin_ids(os.getenv("ADMIN_IDS", "")),
        db_path=os.getenv("DB_PATH", "bot.db").strip() or "bot.db",
    )