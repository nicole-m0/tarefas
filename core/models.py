from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    description = models.CharField('Descrição', max_length=30)
    data_add = models.DateField('Data de criação', auto_now=True)
    done = models.BooleanField('Feita', default=False)
    owner = models.ForeignKey(related_name='Dono', to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'