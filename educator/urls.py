from django.conf.urls import patterns, url

from educator import views

urlpatterns = patterns('',
 

    url(r'^home$', views.educator_home, name='home'),
    url(r'^add_student$', views.add_student, name='add_student') ,
    url(r'^add_parent/(?P<student>[a-zA-Z0-9_.-]+)$', views.add_parent, name='add_parent'),     
    
    
)




