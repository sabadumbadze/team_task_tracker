from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskReadSerializer, TaskWriteSerializer
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_done', 'tags__name']
    ordering_fields = ['title', 'id', 'is_done']

    def get_queryset(self):
        user_team = self.request.user.profile.team
        return Task.objects.filter(team=user_team).select_related(
            'team', 'assignee', 'assignee__user'
        ).prefetch_related('tags')

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TaskReadSerializer
        return TaskWriteSerializer
