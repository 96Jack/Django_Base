from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_app(request):
    return HttpResponse(" this is a App index")

def app_html(request):
    return render(request, template_name='score.html')    

def pro_html(request):
    return render(request, template_name='base.html')    