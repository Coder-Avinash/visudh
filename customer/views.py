from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import  CustomerProfileForm, CustomerForm
from .models import Customer_Profile
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages, auth
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# def cust_register(request):
#     context ={}
#     template = 'customer/register.html'
#     form = CustomerForm(request.POST or None)
#     if form.is_valid():
#
#         if Customer.objects.filter(username=form.cleaned_data['username']).exists():
#             return render(request, template, {
#                 'form': form,
#                 'error_message': 'Username already exists.'
#             })
#
#         elif Customer.objects.filter(email=form.cleaned_data['email']).exists():
#             return render(request, template, {
#                 'form': form,
#                 'error_message': 'Email already exists.'
#             })
#
#         elif Customer.objects.filter(phone_number=form.cleaned_data['phone_number']).exists():
#             return render(request, template, {
#                 'form': form,
#                 'error_message': 'Phone number already exists.'
#             })
#
#         elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
#             return render(request, template, {
#                 'form': form,
#                 'error_message': 'Passwords do not match.'
#             })
#
#         else:
#             form.save()
#
#
#             # redirect to accounts page:
#             return HttpResponseRedirect('/customer/account/')
#     else:
#         context['form']= form
#         return render(request, 'customer/register.html', context)



def cust_register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    template = 'customer/register.html'

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        customer_form = CustomerForm(data=request.POST)
        profile_form = CustomerProfileForm(data=request.POST)

        # If the two forms are valid...
        if customer_form.is_valid() and profile_form.is_valid():


            # Save the user's form data to the database.
            user = customer_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            login(request, user)
            return HttpResponseRedirect('/card/')


        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (customer_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        customer_form = CustomerForm()
        profile_form = CustomerProfileForm()

    # Render the template depending on the context.
    return render(request,
            'customer/register.html',
            {'customer_form': customer_form, 'profile_form': profile_form, 'registered': registered})



def cust_login(request):
    data={}
    if request.method == 'POST':

            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                id=user.id
                all_details = Customer_Profile.objects.filter(user_id=id)
                for j in all_details:
                    if j.registered_as =="CUS":
                        auth.login(request, user)
                        messages.info(request, f"You are now logged in as {username}")

                        return render(request = request,
                              template_name = "customer/dashboard.html" )

                else:
                    messages.error(request, 'Username or Password is incorrect.')
                    return HttpResponseRedirect("/customer/login/")

            else:
                messages.error(request, 'Username or Password is incorrect.')
                return HttpResponseRedirect("/customer/login/")

        # else:
        #     messages.error(request, "Invalid username or password.")
    form = CustomerForm()
    return render(request = request,
                  template_name = "customer/login.html",
                  context={"form":form})

def cust_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/customer/login")

@login_required(login_url='/customer/login')
def cust_dashboard(request):
    # if request.user.is_authenticated():
    #     form = CustomerForm(request.POST)
    #     return render(request = request,
    #                   template_name = "customer/login.html",
    #                   context={"form":form})
    dashboard = loader.get_template('customer/dashboard.html')
    return  HttpResponse(dashboard.render())
