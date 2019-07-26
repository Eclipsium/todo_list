from rest_framework import serializers

from org_api.models import Organization
from user_api.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'orgName')


class OrganizationDetailSerializer(serializers.ModelSerializer):
    founder = UserSerializer(read_only=True)
    invitedUser = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'orgName', 'founder', 'invitedUser')

