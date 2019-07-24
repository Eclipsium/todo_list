from django.db.models import Q
from rest_framework import generics

from org_api.models import Organization
from org_api.serializers import OrganizationSerializer
from todo_api.models import ToDoTask
from todo_api.serializers import ToDoTaskSerializer


# class TaskList(generics.ListCreateAPIView):
#     serializer_class = ToDoTaskSerializer
#
#     def get_queryset(self):
#         tasks = ToDoTask.objects.filter(creator_org=[org for org in Organization.objects.filter(
#             Q(founder=self.request.user) | Q(invitedUser=self.request.user))])
#
#
#         return tasks
