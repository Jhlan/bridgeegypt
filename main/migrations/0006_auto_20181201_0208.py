# Generated by Django 2.1.3 on 2018-12-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181130_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='description_ar',
            field=models.TextField(blank=True, max_length=1000, verbose_name='page description in arabic'),
        ),
        migrations.AlterField(
            model_name='page',
            name='description_en',
            field=models.TextField(blank=True, max_length=1000, verbose_name='page description in english'),
        ),
    ]
