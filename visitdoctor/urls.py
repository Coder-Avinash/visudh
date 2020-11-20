from django.urls import path
from . import views

app_name = 'visitdoctor'
urlpatterns = [
    path('',views.index, name='index'),
]
