from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') 
    


def base(request):
    title  = "THE BASE PAGE"
    return render(request, "myapp/main.html", {'title': title})

def user_info(request):
    userinfo = {"username": "Geralt", "country": "Kaera Mohren"}

    context = {"userinfo": userinfo, "title": "User Info Page"}
    context_no_title = {"userinfo": userinfo}
    # return render(request, "myapp/user_info.html", context)

    return render(request, "myapp/user_info.html", context_no_title)



