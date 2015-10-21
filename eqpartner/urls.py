import django_filters
from rest_framework import filters
from rest_framework import generics

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from task.models import Task, Client, Organization, TaskComment, Notification, Todo

from django.forms import ModelForm

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

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
    user = UserSerializer(read_only=True)
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
    user = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'creation_date')

class TaskCommentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'creation_date')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'done', 'user', 'description')

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
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Notification.objects.filter(user=user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'done')

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
    queryset = TaskComment.objects.all()
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
    filter_fields = ('id', 'done', 'user')

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'client', ClientViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'taskComment', TaskCommentViewSet)
router.register(r'taskComment2', TaskCommentViewSet2)
router.register(r'user', UserViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'todo', TodoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]