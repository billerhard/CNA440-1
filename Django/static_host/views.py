from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    # return HttpResponse(template.render)
    string_to_pass = "Hello World"
    integer_to_pass = 999
    data_to_pass = {'string_to_pass':string_to_pass, 'integer_to_pass':integer_to_pass}
    return render(request, "index.html", data_to_pass)

def polls(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bootstrap(request):
    return render(request, "bootstrap.html")
