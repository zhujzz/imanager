from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import loader

from django.views.decorators.csrf import csrf_exempt

from src.apps.users.models import User


def login(request):
    return HttpResponse(render(request, 'users/login.html'))


def list_users(request):
    return HttpResponse("user list")

@csrf_exempt
def login_success(request):
    user_list = User.objects.all()
    return HttpResponse(render(request, 'users/loginSucess.html', {'user_list': user_list}))