from django.http import HttpResponse


def greetings_func(request):
    return HttpResponse("Hello, Django!")
