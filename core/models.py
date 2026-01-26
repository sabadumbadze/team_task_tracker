from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, related_name="profiles")
    team = models.ForeignKey(team, on_delete=models.CASCADE, related_name="profiles" )




