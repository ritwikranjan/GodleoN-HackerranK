from rest_framework import serializers
from questionbank.models import Category,Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields =(
            'question_text',
            'question_link'
        )

class CategoryDetailSerializer(serializers.ModelSerializer):
    questions = serializers.ModelField(
        many = True,
        read_only = True,
        view_name = 'question-detail'
    )
    class Meta:
        model = Category
        fields = (
            'category_name',
            'category_description',
            'questions'
        )


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_text',
            'question_link'
        )