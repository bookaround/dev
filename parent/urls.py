from django.conf.urls import patterns, url

from parent import views

urlpatterns = patterns('',
 
    #parent portal follows   
    url(r'select_student', views.select_student_form, name='select_student'), 
    url(r'student_selected', views.student_selected, name='student_selected'),     
    url(r'find', views.find, name='find'),         
    url(r'bookshelf', views.bookshelf, name='bookshelf'),     
    url(r'student_profile', views.student_profile, name='student_profile'),     
    url(r'parent_profile', views.parent_profile, name='parent_profile'),     

    url(r'home', views.parent_home, name='parent_home'), 
    url(r'login', views.parent_login, name='parent_login'),    


)




