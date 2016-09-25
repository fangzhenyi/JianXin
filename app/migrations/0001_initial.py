# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articleNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, verbose_name='\u6807\u9898')),
                ('cover', models.ImageField(help_text='\u7528\u4e8e\u663e\u793a\u5728\u9996\u9875\u8f6e\u64ad', upload_to='web/newscover/', null=True, verbose_name='\u65b0\u95fb\u5c01\u9762(1920*1080)', blank=True)),
                ('showinindex', models.BooleanField(default=False, verbose_name='\u662f\u5426\u9996\u9875\u8f6e\u64ad')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb',
            },
        ),
    ]
