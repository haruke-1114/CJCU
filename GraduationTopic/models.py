from django.db import models

# Create your models here.
class hospital(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    add = models.TextField()
    phone = models.TextField()
    time = models.TextField()

class disease(models.Model):
    disease = models.CharField(max_length=50)
    name = models.TextField()
    solve = models.TextField()
    description = models.TextField()

class statistics(models.Model):
    disease = models.CharField(max_length=50)
    num = models.DateField(null=True, blank=True)
    month = models.CharField(max_length=50)
    year = models.DateField(null=True, blank=True)