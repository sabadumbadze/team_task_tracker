from django.contrib import admin
from .models import Team, Profile, Tag, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'title', 'assignee', 'is_done')
    search_fields = ('title', 'team__name', 'assignee__user__username')
    list_filter = ('is_done', 'team')

admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(Tag)