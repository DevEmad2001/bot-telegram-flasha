from __future__ import annotations

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➕ إضافة دورة", callback_data="course:add"),
                InlineKeyboardButton(text="📦 عرض الدورات", callback_data="course:list"),
            ],
            [
                InlineKeyboardButton(text="📝 إنشاء منشور", callback_data="post:add"),
                InlineKeyboardButton(text="🗂️ عرض المنشورات", callback_data="post:list"),
            ],
            [
                InlineKeyboardButton(text="🚀 نشر الآن", callback_data="publish:start"),
            ],
        ]
    )