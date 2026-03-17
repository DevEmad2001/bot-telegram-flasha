from __future__ import annotations

from dataclasses import dataclass

import aiosqlite


@dataclass(frozen=True)
class Db:
    path: str


async def connect(db: Db) -> aiosqlite.Connection:
    conn = await aiosqlite.connect(db.path)
    await conn.execute("PRAGMA foreign_keys = ON;")
    return conn