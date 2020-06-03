from django.urls import path,include

from .views import CategoryListAPIView, CategoryDetailAPIView, QuestionDetailAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name="category-list"),
    path('<int:pk>/', CategoryDetailAPIView().as_view(), name="category-detail"),
    path('question/<int:pk>/', QuestionDetailAPIView.as_view(), name="question-detail")
]
