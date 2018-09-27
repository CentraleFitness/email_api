from django.db import models

from emailapp.utils import generate_token, TOKEN_LENGTH


ID_INCREMENT_BEGIN = 21428


def id_increment() -> int:
    last_id = NewsletterRecipient.objects.all().order_by('id').last()
    new_id = (last_id + 3 if last_id else ID_INCREMENT_BEGIN)
    return new_id


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
    email = models.EmailField(blank=None)
    firstname = models.CharField(blank=False, max_length=100)
    lastname = models.CharField(blank=False, max_length=100)
    id_email = models.IntegerField(default=id_increment, editable=False, db_index=True)
    token = models.CharField(default=generate_token, max_length=TOKEN_LENGTH)


class NewsletterCategoryOpt(models.Model):
    recipient = models.ForeignKey(NewsletterRecipient, on_delete=models.CASCADE)
    opt_general = models.BooleanField(default=False)
    opt_sales = models.BooleanField(default=False)
    opt_new = models.BooleanField(default=False)
