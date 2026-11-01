from django.contrib import admin
from .models import Category, Author, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'isbn', 'publisher', 'published_year', 'stock')
    list_filter = ('category', 'published_year')
    search_fields = ('title', 'isbn', 'publisher', 'author__first_name', 'author__last_name')
    list_per_page = 15




