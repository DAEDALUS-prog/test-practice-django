from django.shortcuts import render
from django.http import HttpResponse

from .models import Cars

def index(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars,
        'title': 'Список машин',
    }
    return render(request, template_name='audi/index.html', context=context)

