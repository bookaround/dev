# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookaround', '0026_auto_20140927_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plaintext_pw', models.CharField(max_length=100)),
                ('lexile_score', models.IntegerField()),
                ('points', models.IntegerField()),
                ('school_name', models.CharField(max_length=100)),
                ('school_year', models.CharField(max_length=10)),
                ('classroom_number', models.CharField(max_length=10)),
                ('educator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.OneToOneField(related_name=b'student_profile', to='bookaround.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
