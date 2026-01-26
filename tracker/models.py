from django.db import models
from django.contrib.auth.models import User

# Create


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="members")

    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}"


class Tag(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField()

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=250, unique=True)
    assigne = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    is_done = models.BooleanField(default=False)

    class Meta:
        unique_together = ('team', 'tit;e')

        indexes = [
            models.Index(fields=['team', 'is_done']),

        ]

        def __str__(self):
            return self.title
