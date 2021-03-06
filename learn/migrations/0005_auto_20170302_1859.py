# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20170302_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exams',
            options={'ordering': ['name', 'subjects', 'startDate', 'stopDate'], 'verbose_name': 'Exam', 'verbose_name_plural': 'Exams'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.TextField(blank=True, verbose_name="Correct Answer's text"),
        ),
    ]
