# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0010_auto_20140912_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ISBN_10',
        ),
        migrations.AddField(
            model_name='book',
            name='g_VolumeID',
            field=models.CharField(default='d', max_length=30),
            preserve_default=False,
        ),
    ]
