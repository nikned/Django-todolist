from piston.handler import BaseHandler
from piston.utils import rc, require_extended

from todolist.handler.models import TodoItem

def raise_404(method):
    def wrap(*args, **kwargs):
        from django.core.exceptions import ObjectDoesNotExist
        from django.http import Http404
        try:
            return method(*args, **kwargs)
        except ObjectDoesNotExist, ex:
            raise Http404(ex.message)
    return wrap


class TodosHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    fields = ('id', 'todo', 'priority','category','status','created')
    model = TodoItem

    @require_extended
    def create(self, request, *args, **kw):
        data = request.data
        todoObj = self.model(user=request.user, todo=data['todo'],
                priority=data['priority'],created=data['created'],status=data['status'],category=data['category'])
        todoObj.save()
        #resp = rc.CREATED
        return todoObj

    @raise_404
    def read(self, request, todoitem_id=None):
        if todoitem_id:
            todoitem = TodoItem.objects.get(id=todoitem_id, user=request.user)
        else:
            todoitem = TodoItem.objects.filter(user=request.user)
        return todoitem



    @require_extended
    def update(self, request, todoitem_id):
        data = request.data
        todoObj = TodoItem.objects.get(id=todoitem_id, user=request.user)
        todoObj.todo = data['todo']
        todoObj.created=data['created']
        todoObj.priority = data['priority']
        todoObj.status=data['status']
        todoObj.category= data['category']

        todoObj.save()
        return todoObj

    @raise_404
    def delete(self, request, todoitem_id):
        todoObj = TodoItem.objects.get(id=todoitem_id, user=request.user)
        todoObj.delete()
        return rc.DELETED # returns HTTP 204
