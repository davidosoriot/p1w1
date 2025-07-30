from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'David'})

def about(request):
    return HttpResponse('<h1>Welcome to about Page</h1>')