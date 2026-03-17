from __future__ import annotations

from typing import Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject


class AdminOnlyMiddleware(BaseMiddleware):
    def __init__(self, admin_ids: frozenset[int]) -> None:
        self._admin_ids = admin_ids

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict], Awaitable[object]],
        event: TelegramObject,
        data: dict,
    ) -> object:
        user = getattr(event, "from_user", None)
        user_id = getattr(user, "id", None)

        if user_id is None or user_id not in self._admin_ids:
            await _deny(event)
            return None

        return await handler(event, data)


async def _deny(event: TelegramObject) -> None:
    if isinstance(event, Message):
        await event.answer("هذا البوت للأدمن فقط ✅")
    elif isinstance(event, CallbackQuery):
        await event.answer("للأدمن فقط ✅", show_alert=True)