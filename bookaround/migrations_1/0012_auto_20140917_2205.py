# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookaround', '0011_auto_20140914_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='book',
            name='g_VolumeID',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN_10',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN_13',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='bookaround.Author'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='bookaround.Categories'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='extraLarge',
            field=models.URLField(default=b'', max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='large',
            field=models.URLField(default=b'', max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='medium',
            field=models.URLField(default=b'', max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publishedDate',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='small',
            field=models.URLField(default=b'', max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='smallThumbnail',
            field=models.URLField(default=b'', max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.URLField(default=b'', max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
