from rest_framework import serializers
from .models import Task, Team, Profile, Tag
from django.contrib.auth.models import user


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskReadserializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    assignee = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'team', 'assignee', 'tags', 'is_done']


class TaskWriteSerializer(serializers.ModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team')

    assignee_id = serializers.PrimaryKeyRelatedField(
        quetyset=Profile.objects.all(), source='assignee', required=False)
    tag_ids = serializers.PrimaryKeyRelatedField(
        quetyset=Tag.objects.all(), source='tags', many=True, required=False)

    class Meta:
        model = Task
        fields = ['team_id', 'title', 'assignee_id', 'tag_ids', 'is_done']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "სათაური უნდა იყოს მინიმუმ 3 სიმბოლო")

    def validate(self, attrs):
        team = attrs.get('team')
        assignee = attrs.get('assignee')

        if assignee and assignee.team != team:
            raise serializers.ValidationError(
                " 400 უნდა შესრულდეს იგივე გუნდიდან")
