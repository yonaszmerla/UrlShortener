import time

from django.db import models

from .consts import BASE_REDIRECT_URL

# Create your models here.


class ShortUrl(models.Model):
    """
    Model for short url
    The url is generated by adding the timestamp to the base url
    That way we ensure that the url is unique
    """
    url = models.CharField(unique=True, max_length=100, default=BASE_REDIRECT_URL + str(time.time_ns()))
    redirect_url = models.CharField(max_length=200)
    hit_count = models.IntegerField(default=0)
