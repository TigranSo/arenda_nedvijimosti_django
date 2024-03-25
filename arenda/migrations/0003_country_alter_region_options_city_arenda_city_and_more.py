# Generated by Django 4.2.8 on 2023-12-22 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0002_remove_region_name_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Страна')),
            ],
            options={
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name_plural': 'Регионы'},
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Город')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='arenda.country', verbose_name='Страна')),
            ],
            options={
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.AddField(
            model_name='arenda',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arenda.city', verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arenda',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arenda.country', verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='arenda.city', verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arenda.city', verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arenda.country', verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yacht',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arenda.city', verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yacht',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arenda.country', verbose_name='Страна'),
            preserve_default=False,
        ),
    ]
