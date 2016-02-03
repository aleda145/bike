from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hej världen")


# Create your views here.
