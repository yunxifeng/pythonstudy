# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relate', '0003_auto_20181225_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('student_name', models.CharField(max_length=20)),
                ('teachers', models.ManyToManyField(to='relate.Teacher')),
            ],
        ),
    ]
