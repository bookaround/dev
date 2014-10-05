# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0021_auto_20140918_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_read_list',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='am_read_list',
            name='date_last_modified',
        ),
        migrations.RemoveField(
            model_name='have_read_list',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='have_read_list',
            name='date_last_modified',
        ),
        migrations.RemoveField(
            model_name='want_read_list',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='want_read_list',
            name='date_last_modified',
        ),
    ]
