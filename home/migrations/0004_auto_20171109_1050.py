# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='mini_background',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='scenes',
            name='mini_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
