# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0027_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Have_Read_List_Book_Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(to='bookaround.Book')),
                ('have_read_list', models.ForeignKey(to='bookaround.Have_Read_List')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='am_read_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book_rating',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='have_read_list',
            name='book',
            field=models.ManyToManyField(to=b'bookaround.Book', through='bookaround.Have_Read_List_Book_Order'),
        ),
        migrations.AlterField(
            model_name='have_read_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recommendation_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='want_read_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
