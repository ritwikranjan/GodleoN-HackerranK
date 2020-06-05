from rest_framework import serializers
from questionbank.models import Category,Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields =(
            'question_text',
            'question_link'
        )

class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(
        many = True,
    )
    class Meta:
        model = Category
        fields = (
            'category_name',
            'category_description',
            'questions'
        )


class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_text',
            'question_link'
        )