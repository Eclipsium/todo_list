from django.contrib.auth.models import User
from django.db import models

from org_api.models import Organization


class ToDoTask(models.Model):
    creator_org = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    createDate = models.DateTimeField('Дата создания', auto_now_add=True)
    is_complete = models.BooleanField('Выполнено', default=False)
    taskSubject = models.TextField('Текст задания', blank=False)
    completed_with_user = models.ForeignKey(User, verbose_name='Завершено пользователем',
                                            blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.creator_org) + ' - ' + str(self.taskSubject)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
