from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_teams'
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='joined_teams'
    )

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tracker_profile'
    )
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='team_profiles')
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

    description = models.TextField()
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

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
