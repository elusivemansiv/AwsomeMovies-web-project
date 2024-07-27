from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    slug = models.SlugField()
    date = models.DateField()
    # postby =


    def __str__(self):
         return self.title