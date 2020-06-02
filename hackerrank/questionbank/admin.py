from django.contrib import admin
from .models import Category, Question
# Register your models here.

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Category, CategoryAdmin)