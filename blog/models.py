from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# First model is creating a post
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

