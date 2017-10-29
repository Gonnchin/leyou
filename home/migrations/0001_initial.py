# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=20)),
                ('cag_look', models.IntegerField(default=0)),
                ('cag_image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('view_name', models.CharField(max_length=20)),
                ('view_image', models.ImageField(upload_to='')),
                ('view_title', models.CharField(max_length=30)),
                ('view_score', models.IntegerField(null=True, blank=True)),
                ('view_spot', tinymce.models.HTMLField()),
                ('view_introduce', models.CharField(max_length=100)),
                ('view_describe', tinymce.models.HTMLField()),
                ('view_location', tinymce.models.HTMLField()),
                ('view_look', models.IntegerField(default=0)),
                ('view_category', models.ForeignKey(to='home.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
