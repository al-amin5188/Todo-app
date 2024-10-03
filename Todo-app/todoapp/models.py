from django.db import models

# Create your models here.

class TodoApp(models.Model):
    title= models.TextField(max_length=40)
    detels= models.TextField(max_length=200)
    time= models.DateField()


