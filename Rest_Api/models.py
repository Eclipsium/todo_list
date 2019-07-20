from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    founder = models.ForeignKey(User, verbose_name='Создатель организации', on_delete=models.CASCADE)
    orgName = models.CharField('Название организации', max_length=50)
    invitedUser = models.ManyToManyField(User, related_name='invitedUsers', blank=True, default=User)

    def __str__(self):
        return str(self.orgName)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class ToDoTask(models.Model):
    creator = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    createDate = models.DateTimeField('Дата создания', auto_now_add=True)
    is_complete = models.BooleanField('Выполнено', default=False)
    taskSubject = models.TextField('Текст задания', blank=False)

    def __str__(self):
        return str(self.creator) + ' - ' + str(self.taskSubject)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
