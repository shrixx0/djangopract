from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return HttpResponse("hey im your django server")


def show(request):
    return render()