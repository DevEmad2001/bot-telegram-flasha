"""Router for the /id command – returns user, chat, and type information."""
from __future__ import annotations

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="id")


@router.message(Command("id"))
async def cmd_id(message: Message) -> None:
    """Reply with caller's user_id, chat_id, chat_type, and optional chat title."""
    user = message.from_user
    chat = message.chat

    user_id: int | str = user.id if user else "N/A"
    chat_id: int = chat.id
    chat_type: str = chat.type
    chat_title: str | None = chat.title  # None in private chats

    lines = [
        "🪪 *Identification Info*",
        "",
        f"👤 User ID: `{user_id}`",
        f"💬 Chat ID: `{chat_id}`",
        f"📂 Chat type: `{chat_type}`",
    ]

    if chat_title:
        lines.append(f"🏷 Chat title: *{chat_title}*")

    await message.answer("\n".join(lines), parse_mode="Markdown")

