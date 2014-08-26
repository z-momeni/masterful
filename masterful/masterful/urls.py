from django.conf.urls import *
from django.conf import settings
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', main),
)
