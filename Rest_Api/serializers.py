from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class OrganizationSerializer(serializers.ModelSerializer):
    founder = UserSerializer()
    invitedUser = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'orgName', 'founder', 'invitedUser')


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = ('creator', 'createDate', 'is_complete', 'taskSubject')
