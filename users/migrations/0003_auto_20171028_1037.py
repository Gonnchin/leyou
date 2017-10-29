# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171027_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useralbum',
            old_name='album_title',
            new_name='album_short',
        ),
    ]
