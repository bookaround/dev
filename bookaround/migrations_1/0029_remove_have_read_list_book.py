# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0028_auto_20140928_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='have_read_list',
            name='book',
        ),
    ]
