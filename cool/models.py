from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return {self.name}