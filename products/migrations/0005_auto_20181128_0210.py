# Generated by Django 2.1.3 on 2018-11-28 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181128_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_ar',
            field=models.TextField(help_text='Product Description in Arabic', max_length=1000, verbose_name='description in arabic'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, help_text='Product Description in English', max_length=1000, verbose_name='description in english'),
        ),
    ]
