from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    labtest = loader.get_template('booklabtest/booklabtest.html')
    return  HttpResponse(labtest.render())
