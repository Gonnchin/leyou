# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('travel_title', models.CharField(max_length=20)),
                ('travel_kwd', models.CharField(max_length=20)),
                ('travel_image', models.ImageField(upload_to='')),
                ('content_short', models.CharField(max_length=100)),
                ('travel_content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=30)),
                ('user_pwd', models.CharField(max_length=70)),
                ('user_email', models.CharField(unique=True, max_length=50)),
                ('user_tel', models.CharField(null=True, blank=True, max_length=11)),
                ('user_addr', models.CharField(null=True, blank=True, max_length=50)),
                ('signature', models.CharField(null=True, blank=True, max_length=60)),
                ('gender', models.BooleanField(default=1)),
                ('birthday', models.CharField(null=True, blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='travelnotes',
            name='travel_user',
            field=models.ForeignKey(to='users.User'),
        ),
    ]
