# Generated by Django 2.1.3 on 2018-11-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20181128_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(help_text='Product Name in English', max_length=50, verbose_name='name in english'),
        ),
    ]