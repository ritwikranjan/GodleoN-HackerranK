from rest_framework.generics import ListAPIView,RetrieveAPIView
from questionbank.models import Category,Question

from .serializers import CategoryDetailSerializer, QuestionDetailSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class QuestionDetailAPIView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

    
 
