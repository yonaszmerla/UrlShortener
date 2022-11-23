import datetime
import time

from django.db import models

# Create your models here.

BASE_REDIRECT_URL = 'http://localhost:8000/short/'


class ShortUrl(models.Model):
    url = models.CharField(unique=True, max_length=100, default=BASE_REDIRECT_URL + str(time.time_ns()))
    redirect_url = models.CharField(max_length=200)
    hit_count = models.IntegerField(default=0)
