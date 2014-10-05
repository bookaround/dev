# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0016_book_pagecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(),
        ),
    ]
