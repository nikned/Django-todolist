from django.conf.urls import patterns, include, url

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from handler.todoapi import TodosHandler


# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todolist.handler.views.index', name='index'),
    url(r'^register$', 'todolist.handler.views.register', name='register'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)

#these are the calls which need authentication of the user
auth = HttpBasicAuthentication(realm="API")
todoresource = Resource(TodosHandler, authentication=auth)
urlpatterns += patterns('',
   url(r'^todo/list$', todoresource),
   url(r'^todo/task/(?P<todoitem_id>[^/]+)?$', todoresource),
)

