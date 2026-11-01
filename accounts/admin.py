from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number')
    search_fields = ('user__username', 'phone_number')
    filter_horizontal = ('favorite_categories',)




