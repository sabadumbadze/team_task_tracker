from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskReadserializer, TaskWriteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterest_fields = ['is_done', 'tag_name']
    ordering_fields = ['title', 'id', 'is_done']

    def get_queryset(self):
        user_team = self.request.user.profile.team
        return Task.objects.filter(team=user_team).select_related('team', 'assignee', 'assigneee_user').prefetch_related('tags')

    def get_serializer_class(self):
        if self.action in ['list', 'retrive']:
            return TaskReadserializer
        return TaskWriteSerializer

    def perform_create(self, serializer):
        serializer.save(team=self.request.user.profile.team)
