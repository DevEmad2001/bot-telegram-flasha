"""Course data definitions for the bot."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Instructor:
    """Instructor information."""

    name: str
    title: str
    experience: str
    bio: str


@dataclass
class CourseInfo:
    """Complete course information."""

    id: str
    name_ar: str
    name_en: str
    description: str
    target_audience: list[str]
    duration: str
    days: list[str]
    period: str
    course_system: list[str]
    start_date: str
    original_price: str
    current_price: str
    payment_methods: list[str]
    topics: list[str]
    instructor: Instructor
    registration_url: str
    syllabus_file: Optional[str] = None


# Flasha Team social links
SOCIAL_LINKS = {
    "واتساب": "https://chat.whatsapp.com/J9PmIbCQdFgInUyMRwpBuE?mode=ac_t",
    "فيسبوك": "https://www.facebook.com/share/1EZVnWKq5U/",
    "إنستغرام": "https://www.instagram.com/flasha_team?igsh=NndjbGdmc3hneDRp",
    "لينكدإن": "https://www.linkedin.com/company/flacha-for-software-project-%D9%81%D9%84%D8%A7%D8%B4%D8%A9-%D9%84%D9%84%D9%85%D8%B4%D8%A7%D8%B1%D9%8A%D8%B9-%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D9%8A%D8%A9/",
    "يوتيوب": "https://youtube.com/@flashateam?si=ayV3HVyOn-00w9OG",
    "الموقع": "https://flashateam.com",
}

# Course: .NET Backend
NET_BACKEND_COURSE = CourseInfo(
    id="net_backend",
    name_ar="رحلتك إلى عالم الباك إند - .NET",
    name_en="Your Journey into Back-End Development - .NET",
    description="دورة عملية موجهة للمبتدئين وأصحاب الأساس البرمجي، وتهدف إلى بناء فهم قوي في Backend Development باستخدام .NET، مع مشروع عملي، GitHub، ومهارات يحتاجها سوق العمل.",
    target_audience=[
        "المبتدئون الذين لديهم أساس برمجي",
        "طلبة الجامعات",
        "الخريجون",
        "الراغبون بالتحول إلى مجال Backend",
        "(لا تحتاج خبرة Backend مسبقة)",
    ],
    duration="40 ساعة تدريبية",
    days=["السبت", "الثلاثاء", "يوم ثالث يحدد لاحقًا"],
    period="مسائي",
    course_system=[
        "أونلاين",
        "مسجلة",
        "مشروع نهائي تطبيقي",
        "3 تاسكات أسبوعيًا",
        "Quiz أو امتحان",
        "تقييم نهائي",
        "شهادة حضور",
    ],
    start_date="28 / 3",
    original_price="80 دينار",
    current_price="55 دينار",
    payment_methods=["كليك", "تحويل بنكي", "محفظة إلكترونية", "كاش"],
    topics=[
        "C#",
        "Control Flow",
        "MVC",
        ".NET",
        "OOP",
        "SOLID",
        "LINQ",
        "Entity Framework Core",
        "SQL Server",
        "REST APIs",
        "JWT",
        "Clean Architecture",
        "Git / GitHub",
        "Swagger",
        "Postman",
        "Deployment",
        "Repository Pattern / Unit of Work",
        "Validation / Exception Handling / Logging",
    ],
    instructor=Instructor(
        name="عدي الفرارجه",
        title="Team Lead",
        experience="12 سنة خبرة",
        bio="مهندس برمجيات محترف متخصص في تطوير تطبيقات الويب والخوادم.",
    ),
    registration_url="https://docs.google.com/forms/d/e/1FAIpQLSdVHli-08i80BXHsSlmwdct2vDceufsKEXub7Ai-1I4wi7LHA/viewform",
    syllabus_file=None,  # سيتم تحديثه لاحقًا
)

# Dictionary for easy course lookup
COURSES: dict[str, CourseInfo] = {
    NET_BACKEND_COURSE.id: NET_BACKEND_COURSE,
}


def get_course(course_id: str) -> Optional[CourseInfo]:
    """Get course by ID."""
    return COURSES.get(course_id)


def list_courses() -> list[CourseInfo]:
    """Get all available courses."""
    return list(COURSES.values())

