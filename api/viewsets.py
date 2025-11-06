from core.models import Todo
from api.serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer