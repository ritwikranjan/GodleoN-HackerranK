from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.views import generic


# Create your views here.
class CategoryList(generic.ListView):
    template_name = 'questionbank/index.html'
    def get_queryset(self):
        return Category.objects.all()
    
def question(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    category_list = get_list_or_404(Category.objects)
    context = {
        'category': category,
        'category_list': category_list
    }
    return render(request, 'questionbank/question.html', context)

def base(request):
    return render(request, 'questionbank/base.html')
    
