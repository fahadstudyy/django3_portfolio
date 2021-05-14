from django.db import models

class project(models.Model):
    title = models.CharField(max_length=250)
    descreption = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'portfolio/Image/')
    url = models.URLField(blank=True)
