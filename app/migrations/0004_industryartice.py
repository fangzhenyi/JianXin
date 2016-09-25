# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151205_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryArtice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('intro', models.CharField(max_length=200, verbose_name='\u7b80\u4ecb')),
                ('pic', models.ImageField(upload_to=b'web/news/img', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u884c\u4e1a\u767d\u76ae\u4e66',
            },
        ),
    ]
