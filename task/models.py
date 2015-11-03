from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils import timezone

from redactor.fields import RedactorField

class Module(models.Model):
    tag = models.CharField(max_length=50, verbose_name="Nombre corto")
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __unicode__(self):
        return self.tag + ' - ' + self.name

class Notification(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario')
    ntype = models.CharField(max_length=50, verbose_name="Tipo de notificacion")
    notification = models.IntegerField(verbose_name="Notification")
    read = models.BooleanField(default=0, verbose_name="Leida?");
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.id + ' ' + self.user

class Organization(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    address = models.CharField(max_length=50, verbose_name="Direccion")

    def __unicode__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    address = models.CharField(max_length=50, verbose_name='Direccion')
    telephone = models.IntegerField(verbose_name='Telefono')
    mail = models.EmailField(max_length=254, verbose_name='Mail')
    organization = models.ForeignKey(Organization, verbose_name="Organizacion")

    def __unicode__(self):
        return self.name + ' ' + self.lastname

class Task(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario')
    client = models.ForeignKey(Client, verbose_name='Cliente')
    title = models.CharField(max_length=100, verbose_name='Titulo de la tarea')
    turnover_code = models.CharField(max_length=50, verbose_name='Codigo en Turnover')
    priority = models.IntegerField(verbose_name='Prioridad')
    urgency = models.IntegerField(verbose_name='Urgencia')
    start_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Inicio')
    finish_date = models.DateField(null=True, blank=True, verbose_name='Fecha Comprometida')
    estimation_hours = models.IntegerField(verbose_name='Horas Estimada')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    sar = models.IntegerField(default=0, verbose_name='Incidente')
    done = models.BooleanField(default=0, verbose_name='Completado')
    module = models.ForeignKey(Module, verbose_name="Modulo")
    creation_date = models.DateField(null=True, blank=True,auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task:task_edit', kwargs={'pk': self.pk})

class TaskComment(models.Model):
    task = models.ForeignKey(Task, verbose_name="Tarea")
    user = models.ForeignKey(User, verbose_name="Usuario")
    comment = models.CharField(max_length= 5000, verbose_name="Comentario")
    docfile = models.FileField(upload_to='%Y-%m-%d', null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

class TaskUser(models.Model):
    task = models.ForeignKey(Task)
    user = models.ForeignKey(User)

class Todo(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    user = models.ForeignKey(User, verbose_name="Usuario")
    task = models.ForeignKey(Task, null=True, verbose_name="Tarea")
    done = models.BooleanField(default=0, verbose_name='Completado')
    creation_date = models.DateTimeField(auto_now_add=True)