from django.conf.urls import patterns, url

from student import views

urlpatterns = patterns('',
    url(r'^student_login$', views.student_login, name='student_login'),	
    url(r'^review$', views.review, name='review'),	
    url(r'^find$', views.find, name='find'),	
    url(r'^bookshelf$', views.bookshelf, name='bookshelf'),	
    url(r'^profile$', views.profile, name='profile'),	              
    url(r'^viewbook$', views.viewbook, name='viewbook'),	      
    url(r'^home$', views.home, name='home'),	    	
    url(r'^process_results$', views.process_results, name='process_results'),     
)




