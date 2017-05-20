# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-23 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadersboard',
            name='user_exam',
        ),
        migrations.AlterField(
            model_name='question',
            name='serial_no',
            field=models.IntegerField(help_text='Questions will be shown based on their index, and this index is shown as the question number', verbose_name="Question's index"),
        ),
        migrations.DeleteModel(
            name='LeadersBoard',
        ),
    ]
