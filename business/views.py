from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import  BusinessProfileForm, BusinessForm
from .models import Business_Profile
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages, auth
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def busi_register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    template = 'business/register.html'

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        business_form = BusinessForm(data=request.POST)
        profile_form = BusinessProfileForm(data=request.POST)

        # If the two forms are valid...
        if business_form.is_valid() and profile_form.is_valid():


            # Save the user's form data to the database.
            user = business_form.save()

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
            print (business_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        business_form = BusinessForm()
        profile_form = BusinessProfileForm()

    # Render the template depending on the context.
    return render(request,
            'business/register.html',
            {'business_form': business_form, 'profile_form': profile_form, 'registered': registered})



def busi_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/business/login")





def busi_login(request):
    data={}
    if request.method == 'POST':

            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:

                id=user.id
                all_details = Business_Profile.objects.filter(user_id=id)
                for j in all_details:
                    if j.registered_as =="BUSI":
                        auth.login(request, user)
                        messages.info(request, f"You are now logged in as {username}")

                        return render(request = request,
                              template_name = "business/dashboard.html" )

                else:
                    messages.error(request, 'Username or Password is incorrect.')
                    return HttpResponseRedirect("/business/login/")

            else:
                messages.error(request, 'Username or Password is incorrect.')
                return HttpResponseRedirect("/business/login/")

        # else:
        #     messages.error(request, "Invalid username or password.")
    form = BusinessForm()
    return render(request = request,
                  template_name = "business/login.html",
                  context={"form":form})


@login_required(login_url='/business/login')
def busi_dashboard(request):
    # dashboard = loader.get_template('business/dashboard.html')
    # return  HttpResponse(dashboard.render())
    dashboard = loader.get_template('business/dashboard.html')
    return  HttpResponse(dashboard.render())
