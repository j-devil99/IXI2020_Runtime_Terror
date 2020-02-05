from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name= 'login'),
    path('register', views.signup, name='register'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    path('logout', views.dashboard, name= 'logout'),
    
]