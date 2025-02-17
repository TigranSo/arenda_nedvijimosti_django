# Generated by Django 4.2.8 on 2023-12-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0004_city_name_en_country_name_en_region_name_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='arenda',
            name='Location_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Расположение на английском'),
        ),
        migrations.AddField(
            model_name='arenda',
            name='description_1_en',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском'),
        ),
        migrations.AddField(
            model_name='arenda',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация об объекте на английском'),
        ),
        migrations.AddField(
            model_name='arenda',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название на английском'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_1_en',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация об объекте на английском'),
        ),
        migrations.AddField(
            model_name='news',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название на английском'),
        ),
        migrations.AddField(
            model_name='sale',
            name='Location_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение на английском'),
        ),
        migrations.AddField(
            model_name='sale',
            name='description_1_en',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском'),
        ),
        migrations.AddField(
            model_name='sale',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация об объекте на английском'),
        ),
        migrations.AddField(
            model_name='sale',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название на английском'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='Location_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение на английском'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='description_1_en',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация об объекте на английском'),
        ),
        migrations.AddField(
            model_name='yacht',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название на английском'),
        ),
    ]
