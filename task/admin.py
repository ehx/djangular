from django.contrib import admin
from .models import Task, TaskUser, Client, Organization, TaskComment

admin.site.register(Task)
admin.site.register(Organization)
admin.site.register(Client)
admin.site.register(TaskUser)
admin.site.register(TaskComment)
