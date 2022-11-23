import json
from typing import Union

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import ShortUrl


# Create your views here.


def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, You are at url_generator app')


@csrf_exempt
def create(request: HttpRequest) -> HttpResponse:
    data = request.POST
    if "url" not in data or not data["url"]:
        return HttpResponseBadRequest("Url was not provided or is not valid")
    url = data["url"]
    short_url = ShortUrl(redirect_url=url)
    short_url.save()
    return HttpResponse(short_url.url)


@csrf_exempt
def short(_: HttpRequest, timestamp: int) -> HttpResponse:
    url = 'http://localhost:8000/short/' + str(timestamp)
    try:
        short_url = ShortUrl.objects.get(url=url)
        short_url.hit_count += 1
        short_url.save()
        return HttpResponseRedirect(short_url.redirect_url)
    except ShortUrl.DoesNotExist:
        return HttpResponse('Short url does not exist', status=404)

