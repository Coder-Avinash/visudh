from django.conf.urls import url
from . import views

app_name = 'mymodule' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    url('register/', views.user_register, name='user_register'),
    url('login/', views.user_login, name='user_login'),
    url('logout/', views.user_logout, name='user_logout'),
]
