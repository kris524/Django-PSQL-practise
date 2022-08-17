from .models import Car
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') 
    


def base(request):
    title  = "THE BASE PAGE"
    cars_list = Car.objects.all()

    return render(request, "myapp/main.html", {'title': title, "cars_list": cars_list })

def user_info(request):

    if request.method == 'GET':
        
        # print("request.GET ==>>", request.GET)
        print("request.GET==>>", request.session.get('username', False))

        if request.session.get('username', False):
            userinfo = {
                'username': request.session['username'],
                'country': request.session['country']
            }

        else:
            userinfo = False

        context = {'userinfo': userinfo,
                    'title': 'User Info Page'}
        template = 'myapp/user_info.html'
        return render(request, template, context)
    
    elif request.method == "POST":
        return HttpResponse('POST request here')

def just_form(request):
    if request.method == "GET":
        context = {'title': 'Form Page'}
        template = 'myapp/just_form.html'
        return render(request, template, context)

    elif request.method == "POST":
        print("request.POST==>>", request.POST)
        username = request.POST.get('username')
        country = request.POST.get('country')
        request.session['username'] = username
        request.session['country'] = country

        return redirect(reverse('myapp:user_info'))


def data(request, id):
    car = Car.objects.get(id=id)
    context = {'car': car}
    return render(request, 'myapp/data.html', context)