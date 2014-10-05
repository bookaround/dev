from django.conf.urls import patterns, url

from bookaround import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^educator_register/$', views.educator_register, name='educator_register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),     
)




