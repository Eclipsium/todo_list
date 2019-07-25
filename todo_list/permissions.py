from django.db.models import Q
from rest_framework import permissions

from org_api.models import Organization
from todo_api.models import ToDoTask


class IsCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsFounder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.founder == request.user


class IsFounderOrInvited(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_invited = ToDoTask.objects.filter(creator_org__invitedUser=request.user).exists()

        if obj.creator_org.founder == request.user or is_invited:
            return True
