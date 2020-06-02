from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Category

# Create your views here.
class CategoryList(generic.ListView):
    template_name = 'questionbank/index.html'
    def get_queryset(self):
        return Category.objects.all()
    
    