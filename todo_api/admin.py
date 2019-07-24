from django.contrib import admin
from todo_api.models import *


class ToDoTaskAdmin(admin.ModelAdmin):
    list_display = ('creator_org', 'createDate', 'is_complete', 'taskSubject', 'completed_with_user')


admin.site.register(ToDoTask, ToDoTaskAdmin)

