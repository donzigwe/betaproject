# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-14 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0006_auto_20160908_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]