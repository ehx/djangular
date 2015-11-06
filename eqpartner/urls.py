import django_filters
from rest_framework import filters
from rest_framework import generics

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from task.models import *
from rest_framework.pagination import PageNumberPagination
from django.conf.urls import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'tag', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'ntype', 'notification', 'read')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'sar', 'title', 'description', 'creation_date', 'done', 'start_date', 'finish_date', 'client', 'user',
            'priority', 'urgency', 'estimation_hours', 'module')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization

class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'creation_date', 'docfile')


class TaskCommentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'creation_date', 'docfile')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'done', 'user', 'description', 'task')


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('notification', 'user', 'read')

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'done', 'user', 'client')


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'lastname', 'organization')


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all().order_by('-creation_date')
    serializer_class = TaskCommentSerializer2
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('task', 'user')
    pagination_class = StandardResultsSetPagination


class TaskCommentViewSet2(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('task', 'user')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'done', 'user', 'task')


router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'client', ClientViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'taskComment', TaskCommentViewSet)
router.register(r'taskComment2', TaskCommentViewSet2)
router.register(r'user', UserViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'todo', TodoViewSet)
router.register(r'module', ModuleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken'))
]
