from django.urls import path
from . import views

app_name = 'buymedicine'
urlpatterns = [
    path('', views.index, name='index'),
]
