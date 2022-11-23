from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from .models import ShortUrl


# Create your views here.


def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, You are at url_generator app')


@csrf_exempt
def create(request: HttpRequest) -> HttpResponse:
    """
    Create a short url for the given url
    Stores the short url in database with hit counter
    """
    if request.method == 'POST':
        # get the url from the request
        data = request.POST
        if "url" not in data or not data["url"]:
            return HttpResponseBadRequest("Url was not provided or is not valid")
        url = data["url"]
        # create a short url
        short_url = ShortUrl(redirect_url=url)
        short_url.save()
        # return the short url
        return HttpResponse(short_url.url)
    else:
        return HttpResponseNotAllowed("Only POST method is allowed")


@csrf_exempt
def short(_: HttpRequest, timestamp: int) -> HttpResponse:
    """
    Redirect to the url for the given short url
    Increments the hit counter for the short url
    """
    url = 'http://localhost:8000/short/' + str(timestamp)
    try:
        # get the short url from the database
        short_url = ShortUrl.objects.get(url=url)
        # increment the hit counter
        short_url.hit_count += 1
        short_url.save()
        # redirect to the url
        return HttpResponseRedirect(short_url.redirect_url)
    except ShortUrl.DoesNotExist:
        return HttpResponse('Short url does not exist', status=404)

