from . import views
from django.urls import path



app_name = 'admin'  # here for namespacing of urls.

urlpatterns = [
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("", views.admin_login, name="admin_login"),
    path("customers/", views.cust_list, name="cust_list"),
    path("users/", views.user_list, name="user_list"),
    path("employees/", views.emp_list, name="emp_list"),
    path("businesses/", views.busi_list, name="busi_list"),
]
