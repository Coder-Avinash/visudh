from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    buymeds = loader.get_template('buymedicine/buymedicine.html')
    return  HttpResponse(buymeds.render())
