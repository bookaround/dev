from django import forms

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from bookaround.models import StudentProfile, UserProfile, EducatorProfile, ParentProfile
from bookaround.forms import StudentUserForm, ProfileForm, StudentProfileForm, UserForm




@login_required #eventually replace with @educator_login_required
def educator_home(request):    

            
        template = loader.get_template('educator/home.html')
        
        my_students = StudentProfile.objects.filter(educator = request.user)
        context = RequestContext(request, {
                'my_students' : my_students,
            })
        return HttpResponse(template.render(context))   
# Create your views here.





#work in progress
@login_required #eventually replace with @educator_login_required
def add_parent(request, student):

        
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)    

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
        
            # Save the user's form data to the database.
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            parent_profile = ParentProfile()
            parent_profile.user_profile = profile
            parent_profile.save()
            
            #get the student's user account. sloppy
                 
            #student_profile_form = student_profile_form.save(commit=False)
            #student_profile_form.user_profile = profile
            #student_profile_form.educator = request.user
            #student_profile_form.save()

            #user.set_password(student_profile_form.plaintext_pw)
            #user.save()
            
            # Update our variable to tell the template registration was successful.
            registered = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ProfileForm()


    # Render the template depending on the context.
    return render_to_response(
            'educator/add_parent.html',
            {'forms': [user_form, profile_form], 
            'registered': registered,
            'student': student,},
            context)  
            
            
            


#        my_students = StudentProfile.objects.filter(educator = request.user)
#        context = RequestContext(request, {
#                'capture' : capture,
#            })
#        return HttpResponse(template.render(context))   

@login_required #eventually replace with @educator_login_required
def add_student(request):

    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        student_user_form = StudentUserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        student_profile_form = StudentProfileForm(data=request.POST)        

        # If the two forms are valid...
        if student_user_form.is_valid() and profile_form.is_valid() and student_profile_form.is_valid():
            # Save the user's form data to the database.
            user = student_user_form.save()



            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            student_profile_form = student_profile_form.save(commit=False)
            student_profile_form.user_profile = profile
            student_profile_form.educator = request.user
            student_profile_form.save()

            user.set_password(student_profile_form.plaintext_pw)
            user.save()
            
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print student_user_form.errors, profile_form.errors, student_profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        student_user_form = StudentUserForm()
        profile_form = ProfileForm()
        student_profile_form = StudentProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'educator/add_student.html',
            {'forms': [student_user_form, profile_form, student_profile_form], 'registered': registered},
            context)  