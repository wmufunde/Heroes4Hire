# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-14 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtraining',
            name='description',
            field=models.TextField(default='Please Add Description'),
        ),
        migrations.AlterField(
            model_name='classtraining',
            name='typeofClass',
            field=models.CharField(choices=[('AC', 'Armed Combat'), ('UC', 'Unarmed Combat'), ('P', 'Piloting'), ('O', 'Other')], max_length=5),
        ),
        migrations.AlterField(
            model_name='reportlog',
            name='outcome',
            field=models.CharField(choices=[('P', 'Pass'), ('F', 'Fail')], max_length=1),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='address',
            field=models.TextField(default='Please Add Address'),
        ),
    ]