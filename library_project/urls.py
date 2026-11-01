"""
آدرس‌ها و مسیرهای اصلی پروژه (URLs)
"""

from django.contrib import admin
from django.urls import path, include

# فارسی‌سازی تیتر پنل مدیریت
admin.site.site_header = "پنل مدیریت کتابخانه"
admin.site.site_title = "سامانه کتابخانه"
admin.site.index_title = "مدیریت بخش‌های سیستم"

urlpatterns = [
    path('admin/', admin.site.urls),    # آدرس پنل مدیریت
    path('', include('catalog.urls')),  # آدرس صفحه اصلی به سمت کاتالوگ کتاب‌ها
]


