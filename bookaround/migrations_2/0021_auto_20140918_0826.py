# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0020_auto_20140917_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_read_list',
            name='date_added',
            field=models.DateField(default=datetime.date(2014, 9, 18), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='am_read_list',
            name='date_last_modified',
            field=models.DateField(default=datetime.date(2014, 9, 18), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='have_read_list',
            name='date_added',
            field=models.DateField(default=datetime.date(2014, 9, 18), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='have_read_list',
            name='date_last_modified',
            field=models.DateField(default=datetime.date(2014, 9, 18), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='want_read_list',
            name='date_added',
            field=models.DateField(default=datetime.date(2014, 9, 18), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='want_read_list',
            name='date_last_modified',
            field=models.DateField(default=datetime.date(2014, 9, 18), auto_now=True),
            preserve_default=False,
        ),
    ]
