# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_link',
            field=models.CharField(max_length=256, null=True, verbose_name='\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.CharField(max_length=256, null=True, verbose_name='\u7ad9\u70b9'),
        ),
    ]
