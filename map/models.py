from django.db import models

# Create your models here.
class Alcolshop(models.Model):
    CHOICE = {
        ('patner','파트너'), ('store','스토어')
    }
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70, default='')

    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    alcolshoptype = models.CharField(max_length=20, choices=CHOICE, default='patner')


class Filter(models.Model):
    patner = models.BooleanField(default='True')
    store = models.BooleanField(default='True')