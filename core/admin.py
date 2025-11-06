

from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'done', 'owner']
    list_filter = ['done']

    exclude = ['owner', ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
            obj.owner = request.user
            super().save_model(request,obj,form,change)
