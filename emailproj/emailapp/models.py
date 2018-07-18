from django.db import models

# Create your models here.

class Proximity(models.Model):
    email = models.EmailField(blank=None)
    city = models.CharField(max_length=100)

class Address(models.Model):
    city = models.CharField()
    street = models.CharField(blank=True)
    secondary = models.CharField(blank=True)
    zip_code = models.CharField(blank=False)
    country = models.CharField(blank=False)

class NewsletterRecipient(models.Model):
    email = models.EmailField(blank=None)
    subs_at = models.DateField(auto_now_add=True)
    opt_out = models.BooleanField(default=False)
