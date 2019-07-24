from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    founder = models.ForeignKey(User, verbose_name='Создатель организации', on_delete=models.CASCADE)
    orgName = models.CharField('Название организации', max_length=50, db_index=True)
    invitedUser = models.ManyToManyField(User, related_name='invitedUser', blank=True, default=User)

    def __str__(self):
        return str(self.orgName)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
