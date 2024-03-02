from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import CreateBookForm, CreateCategoryForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = CreateBookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category = CreateCategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form': CreateBookForm(),
        'cat_form': CreateCategoryForm(),
        'all_books': Book.objects.filter(active=True).count(),
        'sold_books': Book.objects.filter(status='sold').count(),
        'rented_books': Book.objects.filter(status='rented').count(),
        'available_books': Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None

    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)



    context = {
        'category': Category.objects.all(),
        'books': search,
        'cat_form': CreateCategoryForm(),
    }
    return render(request, 'pages/books.html', context)

def update_book(request, id):
    book_id = Book.objects.get(id=id)

    if request.method == 'POST':
        update_book = CreateBookForm(request.POST, request.FILES, instance=book_id)

        if update_book.is_valid():
            update_book.save()
            return redirect('/')
    else:
        update_book = CreateBookForm(instance=book_id)

    context = {
        'update_form': update_book,
    }
    
    return render(request, 'pages/update.html', context)

def delete_book(request, id):
    book_id = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')