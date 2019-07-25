from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from org_api.models import Organization
from org_api.serializers import OrganizationSerializer


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


class DeleteOrganization(APIView):

    """ Метод GET отдает организацию, создателем которой вы являетесь
        Метод DELETE удаляет организацию, создателем которой вы являетесь. Удалить может только создатель.
    """

    def get(self, request):
        try:
            organization = Organization.objects.get(founder=request.user)
            serializer = OrganizationSerializer(organization)
            return Response({'response': serializer.data})
        except ObjectDoesNotExist:
            return Response({'error': 'У вас нет созданых организаций'})

    def delete(self, request):
        try:
            organization = Organization.objects.get(founder=request.user)
            organization.delete()
            return Response({'response': 'Организация удалена!'})

        except ObjectDoesNotExist:
            return Response({'error': 'Невозможно удалить организацию, которой не существует'})


class CreateOrganization(APIView):
    """Метод POST получается параметр @name и создает организацию с таким именем.
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
