from django.db import models

# Create your models here.
class People(models.Model):
    person_name =models.CharField(max_length=100)
    person_age = models.IntegerField()