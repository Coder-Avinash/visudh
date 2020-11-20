from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def dashboard(request):
    tasks = loader.get_template('tasks/tasks.html')
    return HttpResponse(tasks.render())


def index(request):
    home=loader.get_template('tasks/index.html')
    return HttpResponse(home.render())
