from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    assignee = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team', 'title'], name='unique_task_per_team')
        ]
        indexes = [
            models.Index(fields=['team', 'is_done']),
        ]

    def __str__(self):
        return self.title
