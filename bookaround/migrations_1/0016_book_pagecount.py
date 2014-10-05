# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0015_remove_book_pagecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
