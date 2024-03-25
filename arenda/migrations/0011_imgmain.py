# Generated by Django 4.2.1 on 2023-12-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0010_city_img_country_img_region_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Текст')),
                ('img_main', models.ImageField(upload_to='img', verbose_name='Главная картина')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Шапка главной страницы',
            },
        ),
    ]
