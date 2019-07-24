from rest_framework import serializers

from .models import ToDoTask


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = ('creator_org', 'createDate', 'is_complete', 'taskSubject', 'completed_with_user')
