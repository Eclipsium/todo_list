# Generated by Django 2.2.3 on 2019-07-20 07:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rest_Api', '0003_auto_20190720_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='invitedUser',
        ),
        migrations.AddField(
            model_name='organization',
            name='invitedUser',
            field=models.ManyToManyField(related_name='invitedUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]