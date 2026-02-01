from rest_framework import serializers
from .models import Task, Team, Tag, Profile
from django.contrib.auth.models import User


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskReadSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    assignee = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'team', 'title', 'assignee', 'tags', 'is_done']

    def get_assignee(self, obj):
        if obj.assignee:
            return {"id": obj.assignee.id, "username": obj.assignee.user.username}
        return None


class TaskWriteSerializer(serializers.ModelSerializer):
    team_id = serializers.IntegerField(write_only=True)
    assignee_id = serializers.IntegerField(required=False, allow_null=True)
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(), required=False, write_only=True)

    class Meta:
        model = Task
        fields = ['team_id', 'title', 'assignee_id', 'tag_ids', 'is_done']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long.")
        return value

    def validate(self, attrs):
        assignee_id = attrs.get('assignee_id')
        team_id = attrs.get('team_id')

        if assignee_id:
            try:
                profile = Profile.objects.get(id=assignee_id)
                if profile.team_id != team_id:
                    raise serializers.ValidationError(
                        "Assignee must belong to the same team as the task.")
            except Profile.DoesNotExist:
                raise serializers.ValidationError("Profile not found.")
        return attrs

    def create(self, validated_data):
        tag_ids = validated_data.pop('tag_ids', [])

        validated_data['team_id'] = validated_data.pop('team_id')
        task = Task.objects.create(**validated_data)
        task.tags.set(tag_ids)
        return task
