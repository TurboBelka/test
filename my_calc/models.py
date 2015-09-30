from django.db import models


# Create your models here.
class MyCalc(models.Model):
    first_num = models.DecimalField(max_digits=5, decimal_places=2)
    second_num = models.DecimalField(max_digits=5, decimal_places=2)
    operation = models.CharField(max_length=2)
    result = models.DecimalField(max_digits=5, decimal_places=2)
