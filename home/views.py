from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>Home App - VS Code Integration Working!</h1>")