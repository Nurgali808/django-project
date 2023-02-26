from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения Meloman.")

def categories(request):
    return HttpResponse("<h1>Жанры книг</h1>")