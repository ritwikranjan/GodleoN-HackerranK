from django.urls import path,include

from . import views

app_name = 'questionbank'

urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.CategoryList.as_view(), name='index'),
    path('index/<int:category_id>/', views.question, name='question')
]