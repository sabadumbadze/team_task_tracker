from django.contrib import admin
from .models import Team, Profile, Tag, Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'title', 'assigne', 'is_done')
    search_fields = ('title', 'team__name', 'assigne__user__username')
    list_display('is_done', 'team')


admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(Tag)
