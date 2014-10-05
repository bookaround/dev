# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0003_student_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='username',
        ),
    ]
