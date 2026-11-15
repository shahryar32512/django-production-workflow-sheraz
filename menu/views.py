from django.http import HttpResponse


def menu_page(request):
    return HttpResponse("<h1>Welcome to Menu App!</h1><p>Menu App is working successfully.</p>")