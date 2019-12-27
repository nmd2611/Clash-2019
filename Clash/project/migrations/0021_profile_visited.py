# Generated by Django 2.2.3 on 2019-09-01 15:01

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_auto_20190901_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='visited',
            field=models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message=None)]),
        ),
    ]