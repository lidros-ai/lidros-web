from django.http import HttpResponse


def ping(request):
    return HttpResponse("announcements app is reachable")