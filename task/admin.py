from django.contrib import admin

# Register your models here.
from .models import Task
from .models import TaskUser
from .models import Client


admin.site.register(Task)
admin.site.register(Client)
admin.site.register(TaskUser)
