from django.contrib import admin
from django.urls import path, include
from .views import index, login, register

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
]