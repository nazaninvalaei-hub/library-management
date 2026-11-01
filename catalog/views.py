from django.shortcuts import render
from .models import Book, Category

def book_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    if category_id:
        books = books.filter(category_id=category_id)

    categories = Category.objects.all()

    context = {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    }
    return render(request, 'catalog/book_list.html', context)
