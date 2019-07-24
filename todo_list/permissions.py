from rest_framework import permissions

from org_api.models import Organization


class IsCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsHaveNotOrganization(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        have_org = Organization.objects.filter(founder=request.user).exists()
        return not have_org
