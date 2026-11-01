"""
تنظیمات پنل مدیریت (Admin) برای اپلیکیشن Loans
پروژه درس برنامه‌نویسی وب - فاز اول
"""

from django.contrib import admin
from .models import Loan, Reservation


# مدیریت رکورد‌های امانت کتاب
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    # ستون‌های نمایشی در جدول امانت‌ها
    list_display = (
        'book',
        'user',
        'loan_date',
        'due_date',
        'return_date',
        'renewal_count',
        'status',
        'check_overdue'
    )

    # فیلترهای کناری بر اساس وضعیت، تاریخ امانت و موعد بازگشت
    list_filter = ('status', 'loan_date', 'due_date')

    # جستجو بر اساس عنوان کتاب، شابک، و نام کاربری
    search_fields = ('book__title', 'book__isbn', 'user__username', 'user__first_name', 'user__last_name')

    # فیلدهای فقط خواندنی (جهت جلوگیری از دستکاری ناخواسته تاریخ‌ها)
    readonly_fields = ('loan_date',)

    # عملیات‌های دسته‌جمعی در پنل ادمین
    actions = ['mark_as_returned']

    @admin.display(description="دارای تأخیر؟", boolean=True)
    def check_overdue(self, obj):
        return obj.is_overdue

    @admin.action(description="ثبت بازگشت کتاب‌های انتخاب‌شده")
    def mark_as_returned(self, request, queryset):
        for loan in queryset:
            if loan.status != 'returned':
                loan.status = 'returned'
                loan.return_date = loan.due_date  # یا تاریخ روز
                loan.save()
                # افزایش نسخه موجود کتاب در کتابخانه
                loan.book.available_copies += 1
                loan.book.save()
        self.message_user(request, "کتاب‌های انتخاب‌شده با موفقیت بازگردانده شدند.")


# مدیریت رکورد‌های رزرو کتاب
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'reserved_date', 'status')
    list_filter = ('status', 'reserved_date')
    search_fields = ('book__title', 'user__username')


