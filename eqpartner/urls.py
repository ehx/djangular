import django_filters
from rest_framework import filters
from rest_framework import generics

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from task.models import Task, Client, Organization

from django.forms import ModelForm

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'sar', 'title', 'description', 'creation_date', 'done', 'start_date', 'finish_date', 'clientId', 'userId', 'priority' ,'urgency', 'estimation_hours')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client        

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'done')

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend,)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (filters.DjangoFilterBackend,)

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'client', ClientViewSet)
router.register(r'organization', OrganizationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]