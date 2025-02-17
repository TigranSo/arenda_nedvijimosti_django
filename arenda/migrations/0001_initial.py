# Generated by Django 4.2.1 on 2023-12-21 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('tel', models.CharField(max_length=60, verbose_name='телефон')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Arenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация об объекте')),
                ('img_main', models.ImageField(upload_to='img', verbose_name='Главная картина')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_6', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_7', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_8', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_9', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_10', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_11', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_12', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_13', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_14', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_15', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_16', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_17', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_18', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_19', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_20', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_21', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('property_type', models.CharField(choices=[('vila', 'вилла'), ('shale', 'шале'), ('apartamenti', 'апартаменты'), ('yaxta', 'яхта')], max_length=15, verbose_name='тип жилья')),
                ('property_type_2', models.CharField(choices=[('rent', 'Аренда'), ('buy', 'Купить')], default='rent', max_length=10, verbose_name='Аренда или Купить?')),
                ('people', models.CharField(blank=True, max_length=50, verbose_name='число гостей')),
                ('rooms', models.CharField(blank=True, max_length=50, null=True, verbose_name='Количество спален')),
                ('shower', models.CharField(blank=True, max_length=50, null=True, verbose_name='Количество ванных комнат')),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена от')),
                ('price_max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена до')),
                ('private_21', models.BooleanField(default=False, verbose_name='Цена от владельца ?')),
                ('square', models.CharField(blank=True, max_length=50, null=True, verbose_name='площадь')),
                ('Location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение')),
                ('private_1', models.BooleanField(default=False, verbose_name='Кондиционер ?')),
                ('private_2', models.BooleanField(default=False, verbose_name='Сейф ?')),
                ('private_3', models.BooleanField(default=False, verbose_name='Паркинг ?')),
                ('private_4', models.BooleanField(default=False, verbose_name='Стерео система ?')),
                ('private_5', models.BooleanField(default=False, verbose_name='DVD ?')),
                ('private_6', models.BooleanField(default=False, verbose_name='Wi-Fi ?')),
                ('private_7', models.BooleanField(default=False, verbose_name='Телевизор ?')),
                ('private_8', models.BooleanField(default=False, verbose_name='Спутниковое TV ?')),
                ('private_9', models.BooleanField(default=False, verbose_name='Барбекю ?')),
                ('private_10', models.BooleanField(default=False, verbose_name='Садовая мебель ?')),
                ('private_11', models.BooleanField(default=False, verbose_name='Офис ?')),
                ('private_12', models.BooleanField(default=False, verbose_name='Камин?')),
                ('private_13', models.BooleanField(default=False, verbose_name='Кинозал?')),
                ('private_14', models.BooleanField(default=False, verbose_name='Сауна ?')),
                ('private_15', models.BooleanField(default=False, verbose_name='Тренажёрный зал ?')),
                ('private_16', models.BooleanField(default=False, verbose_name='Срочно предложения ?')),
                ('private_17', models.BooleanField(default=False, verbose_name='В городе ?')),
                ('private_18', models.BooleanField(default=False, verbose_name='У моря ?')),
                ('private_19', models.BooleanField(default=False, verbose_name='Около подъемника ?')),
                ('private_20', models.BooleanField(default=False, verbose_name='Бассейн ?')),
                ('description_1', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Аренда',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация об объекте')),
                ('img_main', models.ImageField(upload_to='img', verbose_name='Главная картина')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('description_1', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_obj', models.CharField(max_length=100, verbose_name='Название объекта')),
                ('tel', models.CharField(max_length=60, verbose_name='телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('url_film', models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт')),
                ('description_2', models.TextField(blank=True, verbose_name='Примичание')),
                ('date_created_1', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Владелец объекта',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Регион')),
                ('name_en', models.CharField(max_length=100, verbose_name='Регион на английском')),
            ],
            options={
                'verbose_name_plural': 'Регион',
            },
        ),
        migrations.CreateModel(
            name='Yacht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация об объекте')),
                ('img_main', models.ImageField(upload_to='img', verbose_name='Главная картина')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_6', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_7', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_8', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_9', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_10', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_11', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_12', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_13', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_14', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_15', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('shower_k', models.CharField(blank=True, max_length=50, null=True, verbose_name='Число душевых кабин')),
                ('property_type', models.CharField(choices=[('vila', 'вилла'), ('shale', 'шале'), ('apartamenti', 'апартаменты'), ('yaxta', 'яхта')], default='yaxta', max_length=15, verbose_name='тип жилья')),
                ('property_type_2', models.CharField(choices=[('rent', 'Аренда'), ('buy', 'Купить')], max_length=10, verbose_name='Аренда или Купить?')),
                ('year', models.CharField(blank=True, max_length=50, null=True, verbose_name='Год выпуска')),
                ('engine', models.CharField(blank=True, max_length=50, null=True, verbose_name='Двигатель')),
                ('long', models.CharField(blank=True, max_length=50, null=True, verbose_name='Длина ')),
                ('price_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('Location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение')),
                ('description_1', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Owner_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arenda.owner', verbose_name='Владелец объекта')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arenda.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name_plural': 'Чартер Яхт',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация об объекте')),
                ('img_main', models.ImageField(upload_to='img', verbose_name='Главная картина')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_6', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_7', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_8', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_9', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_10', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_11', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_12', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_13', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_14', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('img_15', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Дополнительная картина')),
                ('property_type', models.CharField(choices=[('vila', 'вилла'), ('shale', 'шале'), ('apartamenti', 'апартаменты'), ('yaxta', 'яхта')], max_length=15, verbose_name='тип жилья')),
                ('property_type_2', models.CharField(choices=[('rent', 'Аренда'), ('buy', 'Купить')], default='buy', max_length=10, verbose_name='Аренда или Купить?')),
                ('rooms', models.CharField(blank=True, max_length=50, null=True, verbose_name='Количество спален')),
                ('shower', models.CharField(blank=True, max_length=50, null=True, verbose_name='Количество ванных комнат')),
                ('private_1', models.BooleanField(default=False, verbose_name='Бассейн ?')),
                ('private_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='До моря')),
                ('price_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена продажи, €')),
                ('square', models.CharField(blank=True, max_length=50, null=True, verbose_name='площадь')),
                ('Location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение')),
                ('description_1', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Owner_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arenda.owner', verbose_name='Владелец объекта')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arenda.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name_plural': 'Продажа',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.DateField(verbose_name='Прибытие')),
                ('departure', models.DateField(verbose_name='Выезд')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('preferences', models.TextField(blank=True, null=True, verbose_name='Пожелания')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('arenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='arenda.arenda', verbose_name='объект')),
            ],
            options={
                'verbose_name_plural': 'Бронирование',
            },
        ),
        migrations.AddField(
            model_name='arenda',
            name='Owner_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arenda.owner', verbose_name='Владелец объекта'),
        ),
        migrations.AddField(
            model_name='arenda',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arenda.region', verbose_name='Регион'),
        ),
    ]
