from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='titulo')
    description = models.CharField(max_length=255, verbose_name='descripcion')
    done = models.IntegerField(default=0, verbose_name='completado')
    creation_date = models.DateTimeField(editable=True, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task:task_edit', kwargs={'pk': self.pk})

class TaskUser(models.Model):
    taskId = models.ForeignKey(Task)
    userId = models.ForeignKey(User)