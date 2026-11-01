from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.models import Category


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='کاربر'
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        verbose_name='شماره تماس'
    )
    address = models.TextField(
        blank=True,
        verbose_name='نشانی / آدرس'
    )
    favorite_categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='interested_users',
        verbose_name='دسته‌بندی‌های موردعلاقه'
    )

    class Meta:
        verbose_name = 'پروفایل کاربر'
        verbose_name_plural = 'پروفایل کاربران'

    def __str__(self):
        return f"پروفایل {self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()


