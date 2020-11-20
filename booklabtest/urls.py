from django.urls import path
from . import views

app_name = 'booklabtest'
urlpatterns = [
    path('', views.index, name='index'),
]
