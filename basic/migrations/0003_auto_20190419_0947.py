# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20190417_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='remark',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='file',
            name='qiniu_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='file',
            name='remark',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='remark',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='staff',
            name='bank_card_num',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='staff',
            name='bank_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='staff',
            name='remark',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachitem',
            name='default_price',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachitem',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='teachitem',
            name='remark',
            field=models.CharField(default='', max_length=64),
        ),
    ]