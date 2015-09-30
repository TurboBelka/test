# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycalc',
            name='first_num',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='mycalc',
            name='result',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='mycalc',
            name='second_num',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
