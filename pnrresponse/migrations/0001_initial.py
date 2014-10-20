# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PNRResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pnr', models.IntegerField(max_length=10)),
                ('boarding_point', models.CharField(max_length=3)),
                ('reservation_upto', models.CharField(max_length=3)),
                ('chart', models.BooleanField(default=False)),
                ('cl', models.CharField(max_length=2)),
                ('doj', models.DateField()),
                ('frm', models.CharField(max_length=3)),
                ('to', models.CharField(max_length=3)),
                ('count', models.IntegerField(default=1)),
                ('train_name', models.CharField(max_length=50)),
                ('train_no', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
