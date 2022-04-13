from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request,'index.html',context={'users':users})

def chatPage(request,username):
    user_obj = User.objects.get(username=username)
    users= User.objects.exclude(username=request.user.username)
    return render(request,'main_chat.html',context={'users':users,'user':user_obj})
