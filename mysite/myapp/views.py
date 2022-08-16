from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') 
    


def base(request):
    return render(request, "myapp/main.html")

def user_info(request):
    return render(request, "myapp/user_info.html")



