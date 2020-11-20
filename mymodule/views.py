from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'mymodule/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
    
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()


                # Login the user
                # login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/card/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()


    return render(request, template, {'form': form})


def user_login(request):
    data={}
    if request.method == 'POST':

        # form = RegisterForm(request = request, data=request.POST)
        # if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/tasks/')
            else:
                messages.error(request, 'Username or Password is incorrect.')
                return HttpResponseRedirect("/mymodule/user_login")

        # else:
        #     messages.error(request, "Invalid username or password.")
    form = RegisterForm()
    return render(request = request,
                  template_name = "mymodule/login.html",
                  context={"form":form})


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/mymodule/user_login")
