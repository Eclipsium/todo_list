from rest_framework import serializers


from org_api.serializers import OrganizationSerializer
from .models import ToDoTask


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = ('createDate', 'is_complete', 'taskSubject', 'completed_with_user')


class ToDoTaskDetailSerializer(serializers.ModelSerializer):
    creator_org = OrganizationSerializer(read_only=True)
    completed_with_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ToDoTask
        fields = ('creator_org', 'createDate', 'is_complete', 'taskSubject', 'completed_with_user')

