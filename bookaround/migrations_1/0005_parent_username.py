# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0004_remove_parent_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='username',
            field=models.CharField(default='tammyPenguin', unique=True, max_length=30),
            preserve_default=False,
        ),
    ]
