# Generated by Django 2.1.3 on 2018-11-28 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181128_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Choose Product sub Category Name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductSubCategory', verbose_name='sub category'),
        ),
        migrations.AlterField(
            model_name='productmaincategory',
            name='name_ar',
            field=models.CharField(blank=True, max_length=100, verbose_name='main category in arabic'),
        ),
        migrations.AlterField(
            model_name='productmaincategory',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, verbose_name='main category in english'),
        ),
    ]
