# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_contacts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, validators=[user_contacts.validators.validate_string]),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, validators=[user_contacts.validators.validate_string]),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[user_contacts.validators.validate_string]),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=10, validators=[user_contacts.validators.validate_number]),
        ),
    ]
