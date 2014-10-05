# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0009_auto_20140912_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ISBN_13',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
    ]
