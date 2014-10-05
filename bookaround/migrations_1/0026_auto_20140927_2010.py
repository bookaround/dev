# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0025_auto_20140927_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educatorprofile',
            name='user_profile',
            field=models.OneToOneField(related_name=b'educator_profile', to='bookaround.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
