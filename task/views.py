from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Task

class TaskList(ListView):
	model = Task

class TaskDoneList(ListView):
	model = Task

class TaskCreate(CreateView):
	model = Task
	fields = ['title', 'description', 'creation_date']
	success_url = reverse_lazy('task:task_list')

class TaskUpdate(UpdateView):
	model = Task
	fields = ['title', 'description', 'creation_date']
	success_url = reverse_lazy('task:task_list')

class TaskDelete(DeleteView):
	model = Task
	success_url = reverse_lazy('task:task_list')