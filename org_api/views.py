from django.db import IntegrityError
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from org_api.models import Organization
from org_api.serializers import OrganizationSerializer, OrganizationDetailSerializer
from todo_list.permissions import IsFounder


class AccessibleOrganizations(generics.ListAPIView):
    """API для работа с организацией
    Метод GET возвращает организации пользователя, к которым имеет доступ

    /user/invite/ работает с приглашением пользователей в организацию
    """

    serializer_class = OrganizationSerializer

    def get_queryset(self):
        response = set(Organization.objects.filter(
            Q(founder=self.request.user) |
            Q(invitedUser=self.request.user)))
        return list(response)


class CreateOrganization(APIView):
    """Метод POST получает параметр @name и создает организацию с таким именем.
    Пользователь может создать только одну организацию"""

    def post(self, request):

        if Organization.objects.filter(founder=request.user):
            return Response({'error': 'Пользователь уже имеет организацию'})
        else:
            try:
                Organization.objects.create(founder=request.user, orgName=request.data.get('name'))
                return Response({'response': 'Организация создана!'})
            except IntegrityError:
                return Response({'error': 'Параметры не верны, проверьте спецификацию!'})


class DetailOrganization(generics.RetrieveUpdateDestroyAPIView):
    """
    Методы для редактирования и удаления отдельных организаций.
    """

    serializer_class = OrganizationDetailSerializer
    queryset = Organization.objects.all()
    permission_classes = (IsFounder, )
