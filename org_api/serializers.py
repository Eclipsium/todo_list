from rest_framework import serializers

from org_api.models import Organization
from user_api.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    founder = UserSerializer()
    invitedUser = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'orgName', 'founder', 'invitedUser')
