import datetime

from django.http import HttpResponse
import json
from core.models import Todo
from datetime import datetime, date

#Serializer
class TodoSerializer(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, (date)):
            return o.isoformat()

        return None



from django.shortcuts import render

from tarefas.asgi import application


# Create your views here.
def todo(request,id):

   t = Todo.objects.get(pk=id)

   t = t.__dict__

   del(t['_state'])

   data= json.dumps(t, cls=TodoSerializer)

   return HttpResponse(content=data,
                       content_type='application/json',
                       status=200)