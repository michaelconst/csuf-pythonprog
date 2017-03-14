# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['country', 'name']},
        ),
        migrations.AddField(
            model_name='publisher',
            name='country',
            field=models.CharField(default='US', max_length=20),
        ),
    ]