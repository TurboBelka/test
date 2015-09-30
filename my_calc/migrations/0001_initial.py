# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyCalc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_num', models.IntegerField()),
                ('second_num', models.IntegerField()),
                ('operation', models.CharField(max_length=2)),
                ('result', models.IntegerField()),
            ],
        ),
    ]
