# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='info_image',
            field=models.ImageField(upload_to='', default=''),
        ),
    ]
