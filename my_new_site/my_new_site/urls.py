from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import index1
from login import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_new_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^$', views.index1)
)
