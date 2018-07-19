from django.db import models

# Create your models here.

class Proximity(models.Model):
    email = models.EmailField(blank=None)
    city = models.CharField(max_length=100, db_index=True)

class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128, blank=True)
    secondary = models.CharField(max_length=128, blank=True)
    zip_code = models.CharField(max_length=16, blank=False)
    country = models.CharField(max_length=32, blank=False)

class NewsletterRecipient(models.Model):
    email = models.EmailField(blank=None, db_index=True)
    subs_at = models.DateField(auto_now_add=True)
    opt_out = models.BooleanField(default=False, db_index=True)
