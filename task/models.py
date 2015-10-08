from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    address = models.CharField(max_length=50, verbose_name='Direccion')
    telephone = models.IntegerField(verbose_name='Telefono')
    mail = models.EmailField(max_length=254, verbose_name='Mail')

    def __unicode__(self):
        return self.name + ' ' + self.lastname

class Task(models.Model):
    userId = models.ForeignKey(User, verbose_name='Usuario')
    clientId = models.ForeignKey(Client, verbose_name='Cliente')
    title = models.CharField(max_length=50, verbose_name='Titulo de la tarea')
    creation_date = models.DateField(null=True, blank=True,auto_now_add=True)
    turnover_code = models.CharField(max_length=50, verbose_name='Codigo en Turnover')
    priority = models.IntegerField(verbose_name='Prioridad')
    urgency = models.IntegerField(verbose_name='Urgencia')
    start_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Inicio')
    finish_date = models.DateField(null=True, blank=True, verbose_name='Fecha Comprometida')
    estimation_hours = models.IntegerField(verbose_name='Horas Estimada')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    sar = models.IntegerField(default=0, verbose_name='Incidente')
    done = models.BooleanField(default=0, verbose_name='Completado')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task:task_edit', kwargs={'pk': self.pk})

class TaskUser(models.Model):
    taskId = models.ForeignKey(Task)
    userId = models.ForeignKey(User)