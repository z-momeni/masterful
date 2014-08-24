from django.conf.urls import patterns, include, url
from django.conf import settings 
#from django.contrib import admin
from views import *
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'masterful.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$' , 'masterful.views.login'),
   # url(r'^accounts/auth/$' , 'masterful.views.auth_view'),
    #url(r'^accounts/logout/$' , 'masterful.views.logout'),
    #url(r'^accounts/loggedin/$' , 'masterful.views.loggedin'),
    #url(r'^accounts/invalid/$' , 'masterful.views.invalid_login'),
    (r'^login/$','login.html'),
    (r'^logout/$','logout.html'),
    (r'^loggedin/$','loggedin.html'),
    (r'^invalid_login/$','invalid_login.html'),
 



)
