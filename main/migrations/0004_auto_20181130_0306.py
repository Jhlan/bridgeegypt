# Generated by Django 2.1.3 on 2018-11-30 01:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='_(Phone must be in correct form)', regex='^[a-zA-Z0-9]*$')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of sending'),
        ),
    ]
