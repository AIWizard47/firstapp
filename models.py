from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length =100)
    age = models.IntegerField(2)
    height = models.IntegerField(3)
    weight = models.IntegerField(3)