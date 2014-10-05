# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0024_auto_20140927_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educatorprofile',
            old_name='user',
            new_name='user_profile',
        ),
    ]
