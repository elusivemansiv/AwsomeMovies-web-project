from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    image_url = models.CharField(max_length=2083)
