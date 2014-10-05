# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0012_auto_20140917_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
