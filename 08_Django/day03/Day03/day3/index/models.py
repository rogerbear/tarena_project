from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()
