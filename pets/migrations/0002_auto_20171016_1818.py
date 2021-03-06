# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 18:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
