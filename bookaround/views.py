import requests, json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django import forms

from bookaround.forms import ParentLoginForm, StudentLoginForm, UserForm, ProfileForm, EducatorProfileForm
from bookaround.models import Student, Recommendation_List, Want_Read_List, Am_Read_List, Have_Read_List, Parent










def index(request):
    template = loader.get_template('bookaround/index.html')
    context = RequestContext(request, {
        'parent_login_form' : ParentLoginForm(),
        'student_login_form' : StudentLoginForm()
        })
    return HttpResponse(template.render(context))

def under_construction(request):
    template = loader.get_template('bookaround/under_construction.html')
    context = RequestContext(request, {
        })
    return HttpResponse(template.render(context))    
	   
       
def educator_register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        educator_profile_form = EducatorProfileForm(data=request.POST)        

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid() and educator_profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            educator_profile = educator_profile_form.save(commit=False)
            educator_profile.user_profile = profile
            educator_profile.save()
            
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors, educator_profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        educator_profile_form = EducatorProfileForm()

    # Render the template depending on the context.
    template = 'bookaround/index.html' if registered else 'bookaround/educator_register.html'
    return render_to_response(
            template,
            {'forms': [user_form, profile_form, educator_profile_form], 'registered': registered},
            context)  
           
           
           


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            if user.is_active:
                login(request, user)
                try:
                    y = user.profile.student_profile
                    thisTemplate = 'student:home'
                    print y
                except:
                    thisTemplate = 'educator:home'
                print thisTemplate
                return HttpResponseRedirect(reverse(thisTemplate)) 
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Disabled Account.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('bookaround/login.html', {}, context)

        

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('bookaround:index')) 
           