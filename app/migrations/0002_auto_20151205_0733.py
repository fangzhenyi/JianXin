# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlenews',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='articlenews',
            name='showinindex',
        ),
        migrations.AlterField(
            model_name='articlenews',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9'),
        ),
    ]
