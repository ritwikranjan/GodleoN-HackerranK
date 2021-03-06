from django.urls import path,include

from .views import CategoryListAPIView, QuestionDetailAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name="category-list"),
    path('question/<int:pk>/', QuestionDetailAPIView.as_view(), name="question-detail")
]
