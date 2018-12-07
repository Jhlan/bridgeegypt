# Generated by Django 2.1.3 on 2018-11-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20181130_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmaincategory',
            options={'verbose_name': 'Main Category', 'verbose_name_plural': 'Main Categories'},
        ),
        migrations.AddField(
            model_name='productmaincategory',
            name='cycle_inner_ar',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Inner data in arabic'),
        ),
        migrations.AddField(
            model_name='productmaincategory',
            name='cycle_inner_en',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Inner data  in english'),
        ),
    ]
