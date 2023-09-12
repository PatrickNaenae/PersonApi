# models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200) 
    age = models.IntegerField(default=None)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


