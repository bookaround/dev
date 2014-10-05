# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0019_auto_20140917_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='google_id',
            field=models.CharField(max_length=100),
        ),
    ]
