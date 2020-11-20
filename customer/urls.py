from django.conf.urls import url
from . import views

app_name = 'customer' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    url('register/', views.cust_register, name='cust_register'),
    url('login/', views.cust_login, name='cust_login'),
    url('logout/', views.cust_logout, name='cust_logout'),
    url('dashboard/', views.cust_dashboard, name='cust_dashboard'),

]
