from django import forms
from .models import Book, Category

attrs = {'class': 'form-control'}

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'photo_book', 'photo_author', 'pages', 'price',
            'rental_price_day', 'rental_period', 'total_rental', 'status', 'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'author': forms.TextInput(attrs=attrs),
            'photo_book': forms.FileInput(attrs=attrs),
            'photo_author': forms.FileInput(attrs=attrs),
            'pages': forms.NumberInput(attrs=attrs),
            'price': forms.NumberInput(attrs=attrs),
            'rental_price_day': forms.NumberInput(attrs={'id': 'rental_price_perday', **attrs}),
            'rental_period': forms.NumberInput(attrs={'id': 'rental_period', **attrs}),
            'total_rental': forms.NumberInput(attrs={'id': 'total_rental', **attrs}),
            'status': forms.Select(attrs=attrs),
            'category': forms.Select(attrs=attrs),
        }

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs=attrs)
        }
