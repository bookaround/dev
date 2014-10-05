from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django import forms

from bookaround.models import Student, Recommendation_List, Want_Read_List, Am_Read_List, Have_Read_List, Parent, Featured_Recommendations, Video_Review
from bookaround.forms import ParentLoginForm, StudentLoginForm

def parent_login(request):
    request.session["username"] = request.POST['username']
    request.session["userrole"] = "parent"
    return HttpResponseRedirect(reverse('parent:select_student'))   


def select_student_form(request):
    try:
        parentUsername = request.session["username"]
        parent = Parent.objects.get(username = parentUsername)
        theirStudents = parent.students.all()
        template = loader.get_template('parent/select_student.html')
        context = RequestContext(request, {
                'theirStudents' : theirStudents
            })
        return HttpResponse(template.render(context))  
    except:
        return HttpResponseRedirect(reverse('bookaround:index'))   

def student_selected(request):

    if len(request.POST.getlist('student_select')) > 1:
        request.session["student_selected"] = request.POST.getlist('student_select')[0]
    else:
        request.session["student_selected"] = request.POST['student_select']
    return HttpResponseRedirect(reverse('parent:parent_home'))   

def parent_home(request):    
        parent = Parent.objects.get(username = request.session["username"])
        student = Student.objects.get(username = request.session.get("student_selected"))
        try:
            featured_recs = Featured_Recommendations.objects.filter(parent = parent).get(student = student).book.all()
        except:
            featured_recs = []
        try:    
            student_recent_reviews = Video_Review.objects.filter(student = student).order_by('updatestamp')[0:3]
        except:
            student_recent_reviews = []
        try:   
            rec_for_student = Recommendation_List.objects.get(student = student).book.all()[0:3]
        except:
            rec_for_student = []
            
        template = loader.get_template('parent/home.html')
        context = RequestContext(request, {
            'parent' : parent,
            'student' : student,
            'featured_recs' : featured_recs,
            'student_recent_reviews' : student_recent_reviews,
            'rec_for_student' : rec_for_student,
            })
        return HttpResponse(template.render(context))    


def find(request):    
    parent = Parent.objects.get(username = request.session["username"])
    student = Student.objects.get(username = request.session.get("student_selected"))	
    template = loader.get_template('parent/find.html')
    context = RequestContext(request, {
        'parent' : parent,
        'student' : student,        
        })
    return HttpResponse(template.render(context))      


def bookshelf(request):    
    parent = Parent.objects.get(username = request.session["username"])
    student = Student.objects.get(username = request.session.get("student_selected"))	
    template = loader.get_template('parent/bookshelf.html')
    try:
        am_read_list = Am_Read_List.objects.get(student=student)
        am_read_books = am_read_list.book.all()[0:3]
    except:
        am_read_books = []
    try:
        want_read_list = Want_Read_List.objects.get(student=student)
        want_read_books = want_read_list.book.all()[0:4]    
    except:
        want_read_books = []
    try:
        have_read_list = Have_Read_List.objects.get(student=student)
        have_read_books = have_read_list.book.all()[0:3]
    except:
        have_read_books = []

    context = RequestContext(request, {
        'am_read_books' : am_read_books,
        'want_read_books' : want_read_books,
        'have_read_books' : have_read_books,
        'parent' : parent,
        'student' : student,   
        })

    return HttpResponse(template.render(context)) 


def student_profile(request):    
    parent = Parent.objects.get(username = request.session["username"])
    student = Student.objects.get(username = request.session.get("student_selected"))	
    template = loader.get_template('parent/student_profile.html')
    context = RequestContext(request, {
        'parent' : parent,
        'student' : student,        
        })
    return HttpResponse(template.render(context))  

    
def parent_profile(request):    
    parent = Parent.objects.get(username = request.session["username"])
    student = Student.objects.get(username = request.session.get("student_selected"))	
    all_students = parent.students.all()
    template = loader.get_template('parent/parent_profile.html')	
    context = RequestContext(request, {
        'parent' : parent,
        'student' : student,        
        'all_students' : all_students
        })
    return HttpResponse(template.render(context))  

