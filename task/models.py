from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils import timezone

class Notification(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario')
    ntype = models.CharField(max_length=50, verbose_name="Tipo de notificacion")
    notificationId = models.IntegerField(verbose_name="Id Notification")

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
    organizationId = models.ForeignKey(Organization, verbose_name="Organizacion")

    def __unicode__(self):
        return self.name + ' ' + self.lastname

class Task(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario')
    client = models.ForeignKey(Client, verbose_name='Cliente')
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

class TaskComment(models.Model):
    task = models.ForeignKey(Task, verbose_name="Tarea")
    user = models.ForeignKey(User, verbose_name="Usuario")
    comment = models.CharField(max_length= 500, verbose_name="Comentario")
    creation_date = models.DateTimeField(auto_now_add=True)

class TaskUser(models.Model):
    task = models.ForeignKey(Task)
    user = models.ForeignKey(User)