from django.urls import path
from . import views

urlpatterns = [
    path('customer_search', views.cust_search, name='cust_search'),
    path('employee_search/', views.emp_search, name='emp_search'),
    path('business_search/', views.busi_search, name='busi_search'),
    path('search/', views.results, name='result'),
    path('generatepdf/', views.generate_pdf, name='generate-pdf'),
    ]
