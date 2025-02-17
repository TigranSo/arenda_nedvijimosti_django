# Generated by Django 4.2.1 on 2023-12-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0008_alter_arenda_property_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='property_type',
            field=models.CharField(choices=[('vila', 'Villa'), ('shale', 'Chalet'), ('apartamenti', 'Apartment'), ('yaxta', 'Yacht')], max_length=15, verbose_name='тип жилья'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='property_type_2',
            field=models.CharField(choices=[('rent', 'Rent'), ('buy', 'Buy')], default='buy', max_length=10, verbose_name='Аренда или Купить?'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='property_type',
            field=models.CharField(choices=[('vila', 'Villa'), ('shale', 'Chalet'), ('apartamenti', 'Apartment'), ('yaxta', 'Yacht')], default='yaxta', max_length=15, verbose_name='тип жилья'),
        ),
        migrations.AlterField(
            model_name='yacht',
            name='property_type_2',
            field=models.CharField(choices=[('rent', 'Rent'), ('buy', 'Buy')], max_length=10, verbose_name='Аренда или Купить?'),
        ),
    ]
