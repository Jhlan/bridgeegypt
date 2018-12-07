# Generated by Django 2.1.3 on 2018-11-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20181130_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsubcategory',
            name='show_footer',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='y', max_length=1, verbose_name='Show Subcategory in footer'),
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='show_home',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='y', max_length=1, verbose_name='Show Subcategory in homepage'),
        ),
    ]
