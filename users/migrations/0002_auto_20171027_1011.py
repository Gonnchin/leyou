# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('image', models.ImageField(default='', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('info_title', models.CharField(max_length=20)),
                ('info_user', models.CharField(max_length=20)),
                ('info_look', models.IntegerField(default=0)),
                ('info_content', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('album_name', models.CharField(max_length=8)),
                ('album_title', models.CharField(max_length=14)),
                ('album_look', models.IntegerField(default=0)),
                ('album_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='travelnotes',
            name='notes_look',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='image_album',
            field=models.ForeignKey(to='users.UserAlbum'),
        ),
    ]
