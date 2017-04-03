# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('wagtailgridder', '0007_auto_20170217_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridindexpage',
            name='featured_grid_item_1',
            field=models.ForeignKey(blank=True, help_text='Add a featured grid item to the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailgridder.GridItem', verbose_name='Grid Items'),
        ),
        migrations.AddField(
            model_name='gridindexpage',
            name='featured_grid_item_2',
            field=models.ForeignKey(blank=True, help_text='Add a second featured grid item to the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailgridder.GridItem', verbose_name='Grid Items'),
        ),
        migrations.AddField(
            model_name='gridindexpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]