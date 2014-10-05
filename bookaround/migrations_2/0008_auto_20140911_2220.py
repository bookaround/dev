# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0007_video_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lexile_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=75),
        ),
    ]
