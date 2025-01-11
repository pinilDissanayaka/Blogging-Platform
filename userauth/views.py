from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the userauth index.")


def login(request):
    return render(request, 
                  "userauth/login.html")


def register(request):
    return render(request, 
                  "userauth/register.html")
