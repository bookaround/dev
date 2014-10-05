# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0005_parent_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Recommendations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdstamp', models.DateField(auto_now_add=True)),
                ('book', models.ManyToManyField(to='bookaround.Book')),
                ('parent', models.ForeignKey(to='bookaround.Parent')),
                ('student', models.ForeignKey(to='bookaround.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
