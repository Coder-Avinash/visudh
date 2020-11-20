from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    visitdoc=loader.get_template('visitdoctor/visitdoctor.html')
    return HttpResponse(visitdoc.render())
