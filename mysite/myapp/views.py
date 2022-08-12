from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    print("Request object:", request)
    print("Request object type:", type(request))

    html_tags = """
    <h1>This is the Home Page</h1>
    <h3>Thanks for visiting</h3>
    <p>MVT means:</p>
    <ul>
        <li>Model</li>
        <li>View</li>
        <li>Template</li>
    </ul>"""
    response = HttpResponse(html_tags)

    return response

