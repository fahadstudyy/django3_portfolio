from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    descreption = models.TextField()
    date = models.DateField()

