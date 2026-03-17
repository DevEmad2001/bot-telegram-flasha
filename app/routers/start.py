from __future__ import annotations

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from app.ui.keyboards import back_to_menu_kb, main_menu_kb

router = Router(name="start")


@router.message(CommandStart())
async def start(message: Message) -> None:
    """Send welcome message with main menu."""
    welcome_text = (
        "🎉 *أهلاً بك في بوت Flasha Team!*\n\n"
        "مرحباً بك في منصتنا التعليمية المتخصصة في تطوير البرمجيات 💻\n\n"
        "من خلال هذا البوت يمكنك:\n"
        "✅ استعراض الدورات المتاحة\n"
        "✅ معرفة التفاصيل الكاملة لكل دورة\n"
        "✅ الاطلاع على محتوى السيلابس\n"
        "✅ التسجيل بسهولة عبر رابط آمن\n\n"
        "اختر من القائمة أدناه للبدء 👇"
    )

    await message.answer(welcome_text, reply_markup=main_menu_kb(), parse_mode="Markdown")


@router.callback_query(lambda c: c.data == "menu:main")
async def back_to_main_menu(callback: CallbackQuery) -> None:
    """Return to main menu from any submenu."""
    welcome_text = (
        "🎉 *قائمة Flasha Team الرئيسية*\n\n"
        "اختر ما تريد أن تتعرف عليه:"
    )

    await callback.message.edit_text(
        welcome_text, reply_markup=main_menu_kb(), parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "info:registration")
async def info_registration(callback: CallbackQuery) -> None:
    """Show registration process information."""
    text = (
        "📋 *خطوات التسجيل في الدورة*\n\n"
        "1️⃣ اختر الدورة التي تريدها من قائمة الدورات\n"
        "2️⃣ اضغط على زر \"🔗 سجل الآن\"\n"
        "3️⃣ ستنقلك لنموذج التسجيل عبر Google Forms\n"
        "4️⃣ ملء بياناتك بصراحة\n"
        "5️⃣ اختر طريقة الدفع المناسبة\n"
        "6️⃣ سيصلك رد تأكيد على البريد الإلكتروني\n\n"
        "⏰ *المدة المتوقعة:* 5 دقائق فقط!\n\n"
        "لأي استفسار، تواصل معنا عبر وسائل التواصل المتاحة 📞"
    )

    await callback.message.edit_text(text, reply_markup=back_to_menu_kb(), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data == "info:about")
async def info_about(callback: CallbackQuery) -> None:
    """Show information about Flasha Team."""
    text = (
        "ℹ️ *عن Flasha Team*\n\n"
        "🚀 *من نحن؟*\n"
        "Flasha Team هي منصة تعليمية متخصصة في تطوير البرمجيات والتحول الرقمي.\n\n"
        "💡 *رسالتنا:*\n"
        "نسعى لتقديم دورات تدريبية عملية عالية الجودة، "
        "تجمع بين المعرفة النظرية والتطبيق العملي، "
        "لتخريج مطورين محترفين قادرين على مواجهة تحديات سوق العمل.\n\n"
        "🎯 *تخصصنا:*\n"
        "Backend Development • Frontend Development • Mobile Development • "
        "Data Science • AI & Machine Learning\n\n"
        "📞 *تواصل معنا:*\n"
        "موقعنا: flashateam.com"
    )

    await callback.message.edit_text(text, reply_markup=back_to_menu_kb(), parse_mode="Markdown")
    await callback.answer()
