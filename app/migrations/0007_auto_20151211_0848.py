# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_articlenews_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlenews',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
        migrations.AlterField(
            model_name='industryarticle',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
    ]
