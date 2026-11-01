from django.db import models
from django.contrib.auth.models import User
from catalog.models import Book
from datetime import date, timedelta


def get_due_date():
    return date.today() + timedelta(days=14)


class Loan(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'امانت داده شده'),
        ('returned', 'بازگردانده شده'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="کتاب")
    borrow_date = models.DateField(auto_now_add=True, verbose_name="تاریخ امانت")
    due_date = models.DateField(default=get_due_date, verbose_name="موعد بازگشت")
    return_date = models.DateField(null=True, blank=True, verbose_name="تاریخ واقعی بازگشت")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed', verbose_name="وضعیت")
    renew_count = models.IntegerField(default=0, verbose_name="تعداد تمدید")

    class Meta:
        verbose_name = "امانت"
        verbose_name_plural = "امانت‌ها"
        ordering = ['-borrow_date']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    @property
    def is_overdue(self):
        if self.status == 'borrowed' and date.today() > self.due_date:
            return True
        return False




