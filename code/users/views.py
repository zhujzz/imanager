from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def login(request):
    return HttpResponse(render(request, 'users/login.html'))


def list_users(request):
    return HttpResponse("user list")
