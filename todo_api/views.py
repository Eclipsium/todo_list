from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from org_api.models import Organization
from todo_api.models import ToDoTask
from todo_api.serializers import ToDoTaskDetailSerializer, ToDoTaskSerializer
from todo_list.permissions import IsFounderOrInvited, IsFounder


class TaskList(generics.ListAPIView):
    """Метод GET отдает задачи, к которым у вас есть доступ. Сначала отдаются невыполненые задачи.
    Для получения детальной информации, используйте "/task/detail/<pk>".
    """
    serializer_class = ToDoTaskSerializer

    def get_queryset(self):
        tasks = ToDoTask.objects.filter(
            creator_org__in=list(Organization.objects.filter(
                Q(founder=self.request.user) | Q(invitedUser=self.request.user)))).order_by('is_complete')

        return tasks


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    """Метод GET отдает задачи, @id которой передана в строке адреса
        Методы PUT и PATCH  обновляет значения полей
        Метод DELETE удаляет задачу

        Доступы к методам имеет только создатель и приглашенный пользователь"""
    permission_classes = (IsFounderOrInvited,)
    serializer_class = ToDoTaskDetailSerializer

    queryset = ToDoTask.objects.all()


class CreateTask(APIView):

    def post(self, request):
        try:
            organization = Organization.objects.get(founder=request.user)
            task_subject = request.data.get('text')
            if not task_subject:
                return Response({'error': 'Параметр text не был передан'})
        except ObjectDoesNotExist:
            return Response({'error': 'У пользователя нет организации'})

        ToDoTask.objects.create(creator_org=organization, taskSubject=task_subject)

        return Response({'response': 'Задача |' + task_subject + '| создана'})

