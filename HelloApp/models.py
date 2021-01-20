from django.db import models

# Create your models here.
class Locale(models.Model):
    state = models.CharField(max_length=200)
    county = models.CharField(max_length=200)