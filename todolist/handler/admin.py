from django.contrib import admin
from django.contrib.auth.models import  Group#
from django.contrib.sites.models import Site

from todolist.handler.models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    fields = ['todo', 'priority','category','status','created']
    
    def queryset(self, request):
        qs = super(TodoItemAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    
    

admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(TodoItem, admin_class=TodoItemAdmin)
