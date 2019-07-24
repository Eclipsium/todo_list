from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from org_api.models import Organization
from todo_list.permissions import IsCurrentUser
from user_api.serializers import UserSerializer


class CurrentUser(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsCurrentUser,)


class InviteUser(APIView):
    """Метод GET возвращает приглашенных в организацию пользователей, в которой вы являетесь создателем

            Метод POST получает параметр @email и добавляет пользователя в органищацию
            Метод DELETE получает параметр @email и удаляет пользователя из организации

        """

    def get_user_to_invite(self, request):
        user_email = request.data.get('email')
        organization, user_to_invite, error = None, None, None

        if not user_email:
            error = {'error': 'Параметр email не передан. Читайте спецификацию'}
        else:
            try:
                user_to_invite = User.objects.get(email=user_email)
                organization = Organization.objects.get(founder=request.user)
            except ObjectDoesNotExist:
                error = {'error': 'Пользователя с таким email не существует, либо у вас нет организации'}
        return organization, user_to_invite, error

    def get(self, request):
        try:
            organization = Organization.objects.get(founder=request.user)
        except ObjectDoesNotExist:
            return Response({'error': 'У вас нет созданной организации'})

        serializer = UserSerializer(organization.invitedUser, many=True)
        return Response({'response': serializer.data})

    def post(self, request):
        (organization, user_to_invite, error) = self.get_user_to_invite(request)
        if error:
            return Response(error)
        if not organization.invitedUser.filter(email=user_to_invite.email):
            organization.invitedUser.add(user_to_invite)
            organization.save()
        else:
            return Response({'error': 'Пользователь ' + user_to_invite.email + ' уже приглашен в организацию'})
        return Response({'request': 'Пользователь ' + user_to_invite.email + ' добавлен '})

    def delete(self, request):
        (organization, user_to_invite, error) = self.get_user_to_invite(request)
        if error:
            return Response(error)
        if organization.invitedUser.filter(email=user_to_invite.email):
            organization.invitedUser.remove(user_to_invite)
            organization.save()
        else:
            return Response({'error': 'Пользователь с ' + user_to_invite.email + ' не состоит в организации'})
        return Response({'request': 'Пользователь ' + user_to_invite.email + ' удален '})

