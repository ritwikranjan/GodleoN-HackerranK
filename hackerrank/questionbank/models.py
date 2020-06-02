from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 250)
    def __str__(self):
        return self.category_name
    

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    question_text = models.CharField(max_length= 250)
    question_link = models.CharField(max_length= 1000)
    def __str__(self):
        return self.question_text

