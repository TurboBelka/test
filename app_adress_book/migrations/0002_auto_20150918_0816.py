# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adress_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='city',
            field=models.ForeignKey(default=0, to='app_adress_book.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=1, to='app_adress_book.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='adress',
            field=models.ManyToManyField(to='app_adress_book.Adress'),
        ),
    ]
