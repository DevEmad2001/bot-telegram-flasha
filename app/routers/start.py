from __future__ import annotations

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.ui.keyboards import main_menu_kb

router = Router(name="start")


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "لوحة التحكم 👇\n"
        "رح نبنيها خطوة خطوة (Clean Code + ملفات متعددة).",
        reply_markup=main_menu_kb(),
    )