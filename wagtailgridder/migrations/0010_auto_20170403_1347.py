# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailgridder', '0009_gridindexpage_logo_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gridindexpage',
            old_name='hero_image',
            new_name='hero_background_image',
        ),
        migrations.RenameField(
            model_name='gridindexpage',
            old_name='logo_image',
            new_name='hero_logo_image',
        ),
        migrations.AddField(
            model_name='gridindexpage',
            name='featured_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gridindexpage',
            name='hero_button_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gridindexpage',
            name='hero_button_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gridindexpage',
            name='hero_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
