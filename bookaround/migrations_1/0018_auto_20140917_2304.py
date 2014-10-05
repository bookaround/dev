# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0017_auto_20140917_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='google_id',
            field=models.CharField(max_length=100, serialize=False),
            preserve_default=False,            
        ),
    ]
