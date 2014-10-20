# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnrresponse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking_status', models.CharField(max_length=30)),
                ('current_status', models.CharField(max_length=30)),
                ('response', models.ForeignKey(to='pnrresponse.PNRResponse')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
