from django.shortcuts import render
from django.views import generic

# Create your views here.
def Login(request):
    return render(request, 'Login.html')


