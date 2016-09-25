# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_industryartice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndustryArtice',
            new_name='IndustryArticle',
        ),
    ]
