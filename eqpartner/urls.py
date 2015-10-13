import django_filters
from rest_framework import filters
from rest_framework import generics

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from task.models import Task, Client, Organization, TaskComments

from django.forms import ModelForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'sar', 'title', 'description', 'creation_date', 'done', 'start_date', 'finish_date', 'client', 'user', 'priority' ,'urgency', 'estimation_hours')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client        

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization

class TaskCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskComments
        fields = ('id', 'task', 'comment', 'creation_date', 'user')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)

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

class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComments.objects.all()
    serializer_class = TaskCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'client', ClientViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'taskComments', TaskCommentViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



# Use this method for the custom field
#def _user(self, obj):
#    user = self.context['request'].user
#    return user.username