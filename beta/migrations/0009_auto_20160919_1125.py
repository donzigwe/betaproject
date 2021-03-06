# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0008_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betatest',
            name='region',
            field=models.CharField(choices=[(b'Northern Africa', b'North Africa'), (b'West Africa', b'West Africa'), (b'Central Africa', b'Central Africa'), (b'East Africa', b'East Africa'), (b'Southern Africa', b'South Africa')], max_length=60),
        ),
        migrations.AlterField(
            model_name='startup',
            name='category',
            field=models.CharField(choices=[(b' ', b' '), (b'Advertising & Marketing', b'Advertising & Marketing'), (b'Agriculture', b'Agriculture'), (b'Auto', b'Auto'), (b'Betting', b'Betting'), (b'Blog & Forum', b'Blog & Forum'), (b'Chat', b'Chat'), (b'Dating', b'Dating'), (b'Deals', b'Deals'), (b'E-Commerce', b'E-Commerce'), (b'Education', b'Education'), (b'Enterprise Software', b'Enterprise Software'), (b'Entertainment', b'Entertainment'), (b'Events', b'Events'), (b'Fashion', b'Fashion'), (b'Fitness', b'Fitness'), (b'Foods', b'Foods'), (b'Game', b'Game'), (b'Government', b'Government'), (b'Health', b'Health'), (b'Job', b'Job'), (b'Market Place', b'Market Place'), (b'Media', b'Media'), (b'Mobile Payment', b'Mobile Payment'), (b'Music & Video', b'Music & Video'), (b'NGO', b'NGO'), (b'Oil and Gas', b'Oil and Gas'), (b'On Demand Services', b'On Demand Services'), (b'Payments', b'Payments'), (b'Printing', b'Printing'), (b'Real Estate', b'Real Estate'), (b'Religion', b'Religion'), (b'Search', b'Search'), (b'Shipping & Logistics', b'Shipping & Logistics'), (b'Social Media', b'Social Media'), (b'Sports', b'Sports'), (b'Travel & Hotels', b'Travel & Hotels'), (b'Web Development', b'Web Development'), (b'Web Hosting', b'Web Hosting')], max_length=30),
        ),
        migrations.AlterField(
            model_name='startup',
            name='region',
            field=models.CharField(choices=[(b'Northern Africa', b'North Africa'), (b'West Africa', b'West Africa'), (b'Central Africa', b'Central Africa'), (b'East Africa', b'East Africa'), (b'Southern Africa', b'South Africa')], max_length=60),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[(b' ', b' '), (b'Live', b'Live'), (b'Private Beta', b'Private Beta'), (b'Public Beta', b'Public Beta'), (b'Under Development', b'Under Development')], max_length=30),
        ),
        migrations.AlterField(
            model_name='tester',
            name='region',
            field=models.CharField(choices=[(b'Northern Africa', b'North Africa'), (b'West Africa', b'West Africa'), (b'Central Africa', b'Central Africa'), (b'East Africa', b'East Africa'), (b'Southern Africa', b'South Africa')], max_length=60),
        ),
    ]
