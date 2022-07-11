from django import views
from django.urls import path 
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:category_id>/', get_categories, name='category'),
]
