from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, We track bugs here.")