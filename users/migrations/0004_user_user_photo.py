# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171028_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
