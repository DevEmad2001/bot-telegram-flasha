from __future__ import annotations

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.data.courses import list_courses


def main_menu_kb() -> InlineKeyboardMarkup:
    """Main menu buttons for the bot."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎓 الدورات المتاحة", callback_data="courses:list")],
            [InlineKeyboardButton(text="❓ كيف أسجل؟", callback_data="info:registration")],
            [InlineKeyboardButton(text="📞 تواصل معنا", callback_data="info:contact")],
            [InlineKeyboardButton(text="ℹ️ عن Flasha Team", callback_data="info:about")],
        ]
    )


def courses_list_kb() -> InlineKeyboardMarkup:
    """List of all available courses."""
    courses = list_courses()
    buttons = []

    for course in courses:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"📚 {course.name_ar}",
                    callback_data=f"course:select:{course.id}",
                )
            ]
        )

    buttons.append([InlineKeyboardButton(text="◀️ رجوع", callback_data="menu:main")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def course_menu_kb(course_id: str) -> InlineKeyboardMarkup:
    """Menu for a single course."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📖 نظرة عامة", callback_data=f"course:overview:{course_id}")],
            [InlineKeyboardButton(text="🎯 ماذا ستتعلم؟", callback_data=f"course:topics:{course_id}")],
            [InlineKeyboardButton(text="👨‍🏫 المدرب", callback_data=f"course:instructor:{course_id}")],
            [InlineKeyboardButton(text="💰 السعر والحجز", callback_data=f"course:pricing:{course_id}")],
            [InlineKeyboardButton(text="📄 السيلابس", callback_data=f"course:syllabus:{course_id}")],
            [InlineKeyboardButton(text="🔗 سجل الآن", callback_data=f"course:register:{course_id}")],
            [InlineKeyboardButton(text="◀️ الدورات", callback_data="courses:list")],
        ]
    )


def contact_links_kb() -> InlineKeyboardMarkup:
    """Social media and contact links for Flasha Team."""
    from app.data.courses import SOCIAL_LINKS

    buttons = []
    for platform, url in SOCIAL_LINKS.items():
        buttons.append(
            [InlineKeyboardButton(text=f"🔗 {platform}", url=url)]
        )

    buttons.append([InlineKeyboardButton(text="◀️ رجوع", callback_data="menu:main")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_menu_kb() -> InlineKeyboardMarkup:
    """Simple back to main menu button."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️ القائمة الرئيسية", callback_data="menu:main")]
        ]
    )