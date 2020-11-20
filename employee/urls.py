
from . import views


from django.urls import path



app_name = 'employee'  # here for namespacing of urls.

urlpatterns = [
    path("dashboard/", views.emp_dashboard, name="emp_dashboard"),
    path("register/", views.emp_register, name="emp_register"),
    path("logout/", views.emp_logout, name="emp_logout"),
    path("login/", views.emp_login, name="emp_login"),
]
