from __future__ import annotations

from app.db.connection import Db, connect


async def init_db(db: Db) -> None:
    conn = await connect(db)
    try:
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            """
        )
        await conn.execute(
            """
            INSERT OR IGNORE INTO meta(key, value)
            VALUES ('schema_version', '1');
            """
        )
        await conn.commit()
    finally:
        await conn.close()