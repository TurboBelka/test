from django.db import models


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=200)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.city_name


class Adress(models.Model):
    adress = models.CharField(max_length=200)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.adress


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_birth = models.DateField()
    adress = models.ManyToManyField(Adress)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
