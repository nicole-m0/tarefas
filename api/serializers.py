from rest_framework import serializers
from core.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        #Fields = ['id', 'description', 'date_add', 'owner']
        fields = '__all__'