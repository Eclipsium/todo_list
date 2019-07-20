from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import *
from .models import *


class CurrentUser(APIView):
    """API для работы с пользователем

    Метод GET возвращает текущего пользователя
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        current_users = User.objects.filter(id=request.user.id)
        serializer = UserSerializer(current_users, many=True)
        return Response({'response': serializer.data})


class CurrentOrganizations(APIView):
    """API для работа с организацией
    Метод GET возвращает организации пользователя, к которым имеет доступ

    Метод POST получает параметр @orgName и создает организацию с таким именем
    Если пользователь создает организацию без параметра, либо пытается создать вторую, получает error message

    Метод DELETE получает параметр @id и удаляет организацию. Удалить может только создатель.
    """

    permission_classes = [permissions.IsAuthenticated, ]

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


class UserInvite(APIView):
    """Метод GET возвращает приглашенных в организацию пользователей, в которой вы являетесь создателем

    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        try:
            organization = Organization.objects.get(founder=request.user)
        except ObjectDoesNotExist:
            return Response({'error': 'У вас нет созданной организации'})

        serializer = UserSerializer(organization.invitedUser, many=True)
        return Response({'response': serializer.data})

    def post(self, request):
        user_email = request.data.get('email')
        user_to_invite = User.objects.get(email=user_email)
        organization = Organization.objects.get(founder=request.user)
        organization.invitedUser.add(user_to_invite)
        organization.save()
        return Response({'request': 'Пользователь ' + user_email + ' добавлен '})
