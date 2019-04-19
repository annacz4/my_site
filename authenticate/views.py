from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import viewsets
from . import serializers
from authenticate.models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = serializers.User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserCreateSerializer
        return serializers.UserSerializer

def get_users(request):
    users = CustomUser.objects.all()
    return render(request, 'authenticate/getusers.html', context = {'USERS': users})

def home(request):
    return render(request, 'authenticate/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request, ('Error - Please Try Again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')


def register_user(request):
    return render(request, 'authenticate/register.html', {})