# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0004_lightshowstep_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightshowstep',
            name='blue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lightshowstep',
            name='green',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lightshowstep',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lightshowstep',
            name='red',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
