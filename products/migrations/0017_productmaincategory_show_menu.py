# Generated by Django 2.1.3 on 2018-11-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20181130_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmaincategory',
            name='show_menu',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='y', help_text='Show Main category in Main menu', max_length=1, verbose_name='Show in menu'),
        ),
    ]
