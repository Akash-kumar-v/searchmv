from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    director = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    stars = models.CharField(max_length=50)
    rating = models.FloatField()

