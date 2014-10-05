# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0008_auto_20140911_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN_10',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN_13',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
