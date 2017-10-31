# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_information_info_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_look',
            field=models.IntegerField(default=0),
        ),
    ]
