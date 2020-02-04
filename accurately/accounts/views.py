from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def login(request):
    return HttpResponse('<html><body>Login</body></html>')