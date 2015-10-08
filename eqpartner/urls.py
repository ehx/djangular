import django_filters
from rest_framework import filters
from rest_framework import generics

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from task.models import Task, Client

from django.forms import ModelForm

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #exclude = ['done']
        fields = ('id', 'sar', 'title', 'description', 'creation_date', 'done', 'start_date', 'finish_date', 'clientId', 'userId', 'priority' ,'urgency', 'estimation_hours')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'done')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend,)

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'client', ClientViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]