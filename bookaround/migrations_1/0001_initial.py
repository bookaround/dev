# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Am_Read_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('cover', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book_Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updatestamp', models.DateField(auto_now=True)),
                ('createdstamp', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(to='bookaround.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Have_Read_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.ManyToManyField(to='bookaround.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30)),
                ('username', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recommendation_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.ManyToManyField(to='bookaround.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('avatar', models.CharField(max_length=30)),
                ('username', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Want_Read_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.ManyToManyField(to='bookaround.Book')),
                ('student', models.ForeignKey(to='bookaround.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recommendation_list',
            name='student',
            field=models.ForeignKey(to='bookaround.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parent',
            name='students',
            field=models.ManyToManyField(to='bookaround.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='have_read_list',
            name='student',
            field=models.ForeignKey(to='bookaround.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book_rating',
            name='student',
            field=models.ForeignKey(to='bookaround.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_read_list',
            name='book',
            field=models.ManyToManyField(to='bookaround.Book'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_read_list',
            name='student',
            field=models.ForeignKey(to='bookaround.Student'),
            preserve_default=True,
        ),
    ]
