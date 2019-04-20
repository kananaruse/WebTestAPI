# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mail',
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='defaulet', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='defaultpassword', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='defaultname', max_length=32),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
