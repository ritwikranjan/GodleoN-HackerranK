from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Manager()
    category_name = models.CharField(max_length = 250)
    category_slug = models.SlugField(unique=True)
    category_description = models.TextField()
    def __str__(self):
        return self.category_name
    

class Question(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length= 250)
    question_link = models.TextField()
    def __str__(self):
        return self.question_text

