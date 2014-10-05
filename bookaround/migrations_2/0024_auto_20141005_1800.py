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
            name='Am_Read_List_Book_Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('am_read_list', models.ForeignKey(to='bookaround.Am_Read_List')),
                ('book', models.ForeignKey(to='bookaround.Book')),
            ],
            options={
                'ordering': ('date_added',),
            },
            bases=(models.Model,),
        ),
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
            name='Have_Read_List_Book_Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(to='bookaround.Book')),
                ('have_read_list', models.ForeignKey(to='bookaround.Have_Read_List')),
            ],
            options={
                'ordering': ('date_added',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recommendation_List_Book_Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(to='bookaround.Book')),
                ('recommendation_list', models.ForeignKey(to='bookaround.Recommendation_List')),
            ],
            options={
                'ordering': ('date_added',),
            },
            bases=(models.Model,),
        ),
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
                ('user', models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Want_Read_List_Book_Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(to='bookaround.Book')),
                ('want_read_list', models.ForeignKey(to='bookaround.Want_Read_List')),
            ],
            options={
                'ordering': ('date_added',),
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
            model_name='studentprofile',
            name='user_profile',
            field=models.OneToOneField(related_name=b'student_profile', to='bookaround.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educatorprofile',
            name='user_profile',
            field=models.OneToOneField(related_name=b'educator_profile', to='bookaround.UserProfile'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='featured_recommendations',
            name='createdstamp',
        ),
        migrations.RemoveField(
            model_name='video_review',
            name='book',
        ),
        migrations.RemoveField(
            model_name='video_review',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='video_review',
            name='student',
        ),
        migrations.AddField(
            model_name='video_review',
            name='video_file',
            field=models.FileField(default='none', upload_to=b'video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='am_read_list',
            name='book',
            field=models.ManyToManyField(to=b'bookaround.Book', through='bookaround.Am_Read_List_Book_Membership'),
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
            model_name='featured_recommendations',
            name='book',
            field=models.ForeignKey(to='bookaround.Book'),
        ),
        migrations.AlterField(
            model_name='have_read_list',
            name='book',
            field=models.ManyToManyField(to=b'bookaround.Book', through='bookaround.Have_Read_List_Book_Membership'),
        ),
        migrations.AlterField(
            model_name='have_read_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recommendation_list',
            name='book',
            field=models.ManyToManyField(to=b'bookaround.Book', through='bookaround.Recommendation_List_Book_Membership'),
        ),
        migrations.AlterField(
            model_name='recommendation_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='want_read_list',
            name='book',
            field=models.ManyToManyField(to=b'bookaround.Book', through='bookaround.Want_Read_List_Book_Membership'),
        ),
        migrations.AlterField(
            model_name='want_read_list',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
