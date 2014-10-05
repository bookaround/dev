# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0002_remove_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='newtonpenguin', unique=True, max_length=30),
            preserve_default=False,
        ),
    ]
