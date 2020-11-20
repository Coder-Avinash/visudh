from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages, auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.template import loader, RequestContext
from customer.models import Customer_Profile
from employee.models import Employee_Profile
from business.models import Business_Profile




def admin_login(request):
    if request.method == 'POST':

            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active and user.is_superuser:
                id=user.id
                auth.login(request, user)
                messages.info(request, f"You are now logged in as {username}")

                return render(request = request,
                      template_name = "admin/dashboard.html" )

            else:
                messages.error(request, 'Username or Password is incorrect.')
                return HttpResponseRedirect("/admin/")

        # else:
        #     messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(request = request,
                  template_name = "admin/login.html",
                  context={"form":form})




def admin_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/admin/")



@login_required(login_url='/admin/login')
def admin_dashboard(request):
    return render(request, "admin/dashboard.html")

@login_required(login_url='/admin/login')
def cust_list(request):

    all_details = Customer_Profile.objects.all()

    for i in all_details:
        cid=i.id

        all_users = User.objects.filter(id=cid)

    return render(request, "admin/customers.html", {"all_users":all_users, "all_details":all_details})



@login_required(login_url='/admin/login')
def user_list(request):
    all_users = User.objects.all()
    return render(request, "admin/users.html", {"all_users":all_users})

@login_required(login_url='/admin/login')
def emp_list(request):
    all_users = User.objects.all()
    return render(request, "admin/employees.html", {"all_users":all_users})


@login_required(login_url='/admin/login')
def busi_list(request):
    all_users = User.objects.all()
    return render(request, "admin/businesses.html", {"all_users":all_users})
