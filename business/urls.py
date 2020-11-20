from django.conf.urls import url
from . import views

app_name = 'business' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    url('register/', views.busi_register, name='busi_register'),
    url('login/', views.busi_login, name='busi_login'),
    url('logout/', views.busi_logout, name='busi_logout'),
    url('dashboard/', views.busi_dashboard, name='busi_dashboard'),

]
