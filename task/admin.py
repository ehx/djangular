from django.contrib import admin
from .models import Task, TaskUser, Client, Organization

admin.site.register(Task)
admin.site.register(Organization)
admin.site.register(Client)
admin.site.register(TaskUser)
