# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151205_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlenews',
            name='intro',
            field=models.TextField(default='', max_length=1000, verbose_name='\u6587\u7ae0\u4ecb\u7ecd'),
        ),
        migrations.AddField(
            model_name='articlenews',
            name='pic',
            field=models.ImageField(default='', upload_to=b'web/news/img', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe'),
        ),
        migrations.AddField(
            model_name='articlenews',
            name='tag',
            field=models.CharField(default='', max_length=20, verbose_name='\u6587\u7ae0\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='articlenews',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
        migrations.AlterField(
            model_name='articlenews',
            name='title',
            field=models.CharField(default='', max_length=1000, verbose_name='\u6807\u9898'),
        ),
    ]
