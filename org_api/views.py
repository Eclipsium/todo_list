from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from org_api.models import Organization
from org_api.serializers import OrganizationSerializer


class CurrentOrganizations(APIView):
    """API для работа с организацией
    Метод GET возвращает организации пользователя, к которым имеет доступ

    Метод POST получает параметр @orgName и создает организацию с таким именем
    Если пользователь создает организацию без параметра, либо пытается создать вторую, получает error message

    Метод DELETE получает параметр @id и удаляет организацию. Удалить может только создатель.

    /user/invite/ работает с приглашением пользователей в организацию
    """

    def get(self, request):
        all_organizations = Organization.objects.filter(Q(founder=request.user) | Q(invitedUser=request.user))
        organizations = set(all_organizations)  # Исключаем повторяющиеся организации
        serializer = OrganizationSerializer(organizations, many=True)
        return Response({'response': serializer.data})

    def post(self, request):

        if Organization.objects.filter(founder=request.user):
            return Response({'error': 'Пользователь уже имеет организацию'})
        else:
            try:
                Organization.objects.create(founder=request.user, orgName=request.data.get('orgName'))
                return Response({'response': 'Организация создана!'})
            except IntegrityError:
                return Response({'error': 'Параметры не верны, проверьте спецификацию!'})

    def delete(self, request):
        org_id = request.data.get('id')
        if not org_id:
            return Response({'error': 'Параметр id отсуствует. Проверьте спецификацию'})
        try:
            organization = Organization.objects.get(id=org_id)
            if organization.founder == request.user:
                organization.delete()
                return Response({'response': 'Организация удалена!'})
            else:
                return Response({'error': 'Недостаточно прав для удаления'})

        except ObjectDoesNotExist:
            return Response({'error': 'Организации не существует'})
