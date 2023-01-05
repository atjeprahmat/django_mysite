from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello selamat datang di django")