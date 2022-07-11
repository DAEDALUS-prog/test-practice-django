from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

from .models import Cars, Category

def index(request):
    cars = Cars.objects.all()
    categories = Category.objects.all()
    context = {
        'cars': cars,
        'title': 'Список машин',
        'categories': categories,

    }
    return render(request, template_name='audi/index.html', context=context)

def get_categories(request, category_id):
    cars = Cars.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'audi/category.html', {'cars': cars, 'categories': categories, 'category': category,})
