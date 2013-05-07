from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^todolist/', 'todolist.views.index', name='home'),
    #url(r'^todolist/add/', 'todolist.views.add', name='add'),
    #url(r'^todolist/delete/', 'todolist.views.delete', name='delete'),
    # url(r'^todolist/', include('todolist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
