from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')