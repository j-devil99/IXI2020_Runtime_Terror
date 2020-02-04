from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User

def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        # messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          #   messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.is_student = True
          User().save()
          #   mail_body = 'Hi ' + first_name + ', welcome to accurately! Keep on checking the '
          #   send_mail('Welcome to accurately', mail_body, 'dogadopt2019@gmail.com', [email], fail_silently=False)
          #  messages.success(request, 'You are now registered and can log in.')
          return redirect('login')
    else:
      #   messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/signup.html')