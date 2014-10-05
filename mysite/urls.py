from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from bookaround import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls', namespace ='student')),       
    url(r'^parent/', include('parent.urls', namespace ='parent')),
    url(r'^educator/', include('educator.urls', namespace ='educator')),    
    url(r'^$', views.under_construction, name='under_construction'),    
    url(r'^bookaround/', include('bookaround.urls', namespace ='bookaround')),         
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
