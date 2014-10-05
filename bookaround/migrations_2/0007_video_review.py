# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0006_featured_recommendations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdstamp', models.DateField(auto_now_add=True)),
                ('updatestamp', models.DateField(auto_now=True)),
                ('filename', models.CharField(max_length=60)),
                ('book', models.ForeignKey(to='bookaround.Book')),
                ('student', models.ForeignKey(to='bookaround.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
