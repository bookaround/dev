# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookaround', '0023_educator'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducatorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=100)),
                ('school_year', models.CharField(max_length=10)),
                ('classroom_number', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('avatar', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='educator',
            name='user',
        ),
        migrations.DeleteModel(
            name='Educator',
        ),
        migrations.AddField(
            model_name='educatorprofile',
            name='user',
            field=models.OneToOneField(to='bookaround.UserProfile'),
            preserve_default=True,
        ),
    ]
