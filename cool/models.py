from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()

    class company(models.Model):
        name = models.CharField(max_length=50)
        email=models.EmailField()
    address=models.TextField()