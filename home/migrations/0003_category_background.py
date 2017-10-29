# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_cag_describe'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
