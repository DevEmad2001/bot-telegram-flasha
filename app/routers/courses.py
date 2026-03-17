"""Router for handling course-related callbacks and interactions."""
from __future__ import annotations

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import FSInputFile

from app.data.courses import get_course
from app.ui.keyboards import contact_links_kb, course_menu_kb, courses_list_kb

router = Router(name="courses")


@router.callback_query(lambda c: c.data == "courses:list")
async def show_courses_list(callback: CallbackQuery) -> None:
    """Display list of all available courses."""
    text = "🎓 *الدورات المتاحة*\n\naختر دورة لعرض التفاصيل:"
    await callback.message.edit_text(text, reply_markup=courses_list_kb(), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:select:"))
async def select_course(callback: CallbackQuery) -> None:
    """Show course introduction when selected."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    text = (
        f"*{course.name_ar}*\n"
        f"_{course.name_en}_\n\n"
        f"📝 {course.description}\n\n"
        f"⏱️ المدة: {course.duration}\n"
        f"📅 موعد البداية: {course.start_date}\n\n"
        "اختر القسم الذي تريد معرفة المزيد عنه:"
    )

    await callback.message.edit_text(text, reply_markup=course_menu_kb(course_id), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:overview:"))
async def course_overview(callback: CallbackQuery) -> None:
    """Show course overview information."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    text = (
        f"*📖 نظرة عامة على الدورة*\n\n"
        f"*الاسم:*\n{course.name_ar}\n_{course.name_en}_\n\n"
        f"*الوصف:*\n{course.description}\n\n"
        f"*الفئة المستهدفة:*\n"
    )

    for audience in course.target_audience:
        text += f"• {audience}\n"

    text += (
        f"\n*معلومات الدورة:*\n"
        f"⏱️ المدة: {course.duration}\n"
        f"📅 الأيام: {', '.join(course.days)}\n"
        f"🕐 الفترة: {course.period}\n"
        f"📅 موعد البداية: {course.start_date}\n\n"
        f"*نظام الدورة:*\n"
    )

    for system in course.course_system:
        text += f"✓ {system}\n"

    await callback.message.edit_text(text, reply_markup=course_menu_kb(course_id), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:topics:"))
async def course_topics(callback: CallbackQuery) -> None:
    """Show learning outcomes and topics."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    text = f"*🎯 ماذا ستتعلم في {course.name_ar}؟*\n\n"

    for topic in course.topics:
        text += f"✨ {topic}\n"

    text += f"\nستتقن {len(course.topics)} مهارة أساسية من المهارات المطلوبة في سوق العمل! 🚀"

    await callback.message.edit_text(text, reply_markup=course_menu_kb(course_id), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:instructor:"))
async def course_instructor(callback: CallbackQuery) -> None:
    """Show instructor information."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    instructor = course.instructor
    text = (
        f"*👨‍🏫 المدرب*\n\n"
        f"*الاسم:* {instructor.name}\n"
        f"*المسمى الوظيفي:* {instructor.title}\n"
        f"*الخبرة:* {instructor.experience}\n\n"
        f"*عن المدرب:*\n"
        f"{instructor.bio}\n\n"
        f"سيتعلم منه الحضور أفضل الممارسات والمعايير الحديثة في مجال {course.name_ar} ✨"
    )

    await callback.message.edit_text(text, reply_markup=course_menu_kb(course_id), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:pricing:"))
async def course_pricing(callback: CallbackQuery) -> None:
    """Show pricing and payment information."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    text = (
        f"*💰 السعر والحجز*\n\n"
        f"*السعر الأصلي:* ~~{course.original_price}~~\n"
        f"*السعر الخاص الآن:* *{course.current_price}* 🎉\n\n"
        f"_الخصم متاح لمرة واحدة فقط_\n\n"
        f"*طرق الدفع المتاحة:*\n"
    )

    for method in course.payment_methods:
        text += f"✓ {method}\n"

    text += (
        f"\n*معلومات إضافية:*\n"
        f"• يمكن الدفع كاملًا أو بدفع عربون\n"
        f"• سيصلك تفاصيل الدفع بعد التسجيل\n"
        f"• دعم فني متاح طوال فترة الدورة\n\n"
        f"🔗 اضغط على \"سجل الآن\" للبدء"
    )

    await callback.message.edit_text(text, reply_markup=course_menu_kb(course_id), parse_mode="Markdown")
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:syllabus:"))
async def course_syllabus(callback: CallbackQuery) -> None:
    """Send course syllabus PDF or message."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    if course.syllabus_file:
        # If syllabus file exists, send it
        syllabus_doc = FSInputFile(course.syllabus_file)
        await callback.message.answer_document(
            syllabus_doc,
            caption=f"📄 السيلابس الكامل - {course.name_ar}\n\n"
                    f"هذا هو محتوى الدورة بالتفصيل",
        )
        await callback.answer("✅ تم إرسال السيلابس")
    else:
        # If no file, show message
        text = (
            f"📄 *السيلابس - {course.name_ar}*\n\n"
            f"السيلابس سيصل إليك بعد تأكيد التسجيل مباشرة.\n\n"
            f"المحتوى الكامل للدورة يتضمن:\n"
            f"✓ المحاضرات المنظمة\n"
            f"✓ التمارين العملية\n"
            f"✓ المشروع النهائي\n"
            f"✓ المراجع والموارد التعليمية\n\n"
            f"📞 لأي استفسار عن المحتوى، تواصل معنا!"
        )

        await callback.message.edit_text(text, reply_markup=course_menu_kb(course_id), parse_mode="Markdown")
        await callback.answer()


@router.callback_query(lambda c: c.data.startswith("course:register:"))
async def course_register(callback: CallbackQuery) -> None:
    """Show registration link."""
    course_id = callback.data.split(":")[-1]
    course = get_course(course_id)

    if not course:
        await callback.answer("❌ الدورة غير موجودة", show_alert=True)
        return

    text = (
        f"🔗 *التسجيل في {course.name_ar}*\n\n"
        f"لتسجيل دخولك في الدورة، اضغط على الزر أدناه:\n"
        f"سيتم نقلك لنموذج التسجيل الآمن (Google Form)\n\n"
        f"*الخطوات السريعة:*\n"
        f"1. اضغط على \"🔗 فتح نموذج التسجيل\"\n"
        f"2. ملء البيانات المطلوبة\n"
        f"3. اختر طريقة الدفع\n"
        f"4. سجل!\n\n"
        f"⏱️ لن تستغرق سوى 5 دقائق"
    )

    register_kb = (
        __import__("aiogram.types", fromlist=["InlineKeyboardMarkup"]).InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    __import__("aiogram.types", fromlist=["InlineKeyboardButton"]).InlineKeyboardButton(
                        text="🔗 فتح نموذج التسجيل",
                        url=course.registration_url,
                    )
                ],
                [
                    __import__("aiogram.types", fromlist=["InlineKeyboardButton"]).InlineKeyboardButton(
                        text="◀️ رجوع",
                        callback_data=f"course:select:{course_id}",
                    )
                ],
            ]
        )
    )

    await callback.message.edit_text(text, reply_markup=register_kb, parse_mode="Markdown")
    await callback.answer("🔗 اضغط على الزر الأزرق لفتح نموذج التسجيل")


@router.callback_query(lambda c: c.data == "info:contact")
async def info_contact(callback: CallbackQuery) -> None:
    """Show contact information."""
    text = (
        "📞 *تواصل معنا - Flasha Team*\n\n"
        "يسعدنا تواصلك معنا عبر وسائل التواصل المتعددة:\n\n"
    )

    await callback.message.edit_text(text, reply_markup=contact_links_kb(), parse_mode="Markdown")
    await callback.answer()




