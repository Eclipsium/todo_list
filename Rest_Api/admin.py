from django.contrib import admin
from Rest_Api.models import *


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('founder', 'orgName')
    filter_horizontal = ('invitedUser',)


class ToDoTaskAdmin(admin.ModelAdmin):
    list_display = ('creator', 'createDate', 'is_complete', 'taskSubject')


admin.site.register(ToDoTask, ToDoTaskAdmin)
admin.site.register(Organization, OrganizationAdmin)
