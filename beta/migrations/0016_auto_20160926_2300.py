# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-26 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0015_auto_20160926_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='status',
        ),
        migrations.AlterField(
            model_name='startup',
            name='stat',
            field=models.CharField(choices=[(b' ', b' '), (b'Under Development', b'Under Development'), (b'Private Beta', b'Private Beta'), (b'Public Beta', b'Public Beta'), (b'Live', b'Live')], max_length=30),
        ),
    ]