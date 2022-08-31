from django.shortcuts import render

# Parte 01
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Fim da parte 01

# Create your views here.
