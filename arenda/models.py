from _decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Owner(models.Model):
    name_obj = models.CharField(max_length=100, verbose_name='Название объекта')
    tel = models.CharField(max_length=60, verbose_name='телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    url_film = models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт')
    description_2 = models.TextField(blank=True, verbose_name='Примичание')
    date_created_1 = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Владелец объекта'

    def __str__(self):
        return f'{self.name_obj} - {self.tel}'
    

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Страна')
    name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна на английском')
    img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Картина')
    popular = models.BooleanField(default=False, blank=False, verbose_name='Популярные направления ?')
    
    
    class Meta:
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Город')
    name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город на английском')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Страна')
    img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Картина')
    popular = models.BooleanField(default=False, blank=False, verbose_name='Популярные направления ?')
    
    class Meta:
        verbose_name_plural = 'Города'

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name='Регион')
    name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name='Регион на английском')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='regions', verbose_name='Город')
    img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Картина')
    popular = models.BooleanField(default=False, blank=False, verbose_name='Популярные направления ?')
    
    class Meta:
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f"{self.name}"


class Arenda(models.Model):
    PROPERTY_CHOICES = [
        ('vila', _('Villa')),  
        ('shale', _('Chalet')),  
        ('apartamenti', _('Apartment')),  
        ('yaxta', _('Yacht')), 
    ]
    PROPERTY_CHOICES_2 = [
        ('rent', _('Rent')),  
        ('buy', _('Buy')),  
    ]
    
    Owner_object = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец объекта')
    name = models.CharField(max_length=100, verbose_name='Название')
    name_en = models.CharField(max_length=100, verbose_name='Название на английском')
    description = models.TextField(verbose_name='Информация об объекте')
    description_en = models.TextField(verbose_name='Информация об объекте на английском')
    
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Главная картина')
    img_1 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_2 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_3 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_4 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_5 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_6 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_7 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_8 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_9 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_10 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_11 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_12 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_13 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_14 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_15 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_16 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_17 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_18 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_19 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_20 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_21 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    # region_en = models.ForeignKey(Region, on_delete=models.CASCADE, to_field='name_en', verbose_name='Регион на английском')
    
    property_type = models.CharField(max_length=15, choices=PROPERTY_CHOICES, verbose_name='тип жилья')
    property_type_2 = models.CharField(max_length=10, choices=PROPERTY_CHOICES_2, default='rent', verbose_name='Аренда или Купить?')
    people = models.CharField(max_length=50, blank=True, verbose_name='число гостей')
    rooms = models.CharField(max_length=50, blank=True, null=True, verbose_name='Количество спален')
    shower = models.CharField(max_length=50, blank=True, null=True, verbose_name='Количество ванных комнат')
    price_min = models.DecimalField(max_digits=10, blank=False, decimal_places=2, verbose_name='Цена от')
    price_max = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name='Цена до')
    private_21 = models.BooleanField(default=False, blank=False, verbose_name='Цена от владельца ?')
    square = models.CharField(max_length=50,blank=True, null=True, verbose_name='площадь')
    Location = models.CharField(max_length=200, verbose_name='Расположение')
    Location_en = models.CharField(max_length=100, verbose_name='Расположение на английском')
    
    private_1 = models.BooleanField(default=False, blank=False, verbose_name='Кондиционер ?')
    private_2 = models.BooleanField(default=False, blank=False, verbose_name='Сейф ?')
    private_3 = models.BooleanField(default=False, blank=False, verbose_name='Паркинг ?')
    private_4 = models.BooleanField(default=False, blank=False, verbose_name='Стерео система ?')
    private_5 = models.BooleanField(default=False, blank=False, verbose_name='DVD ?')
    private_6 = models.BooleanField(default=False, blank=False, verbose_name='Wi-Fi ?')
    private_7 = models.BooleanField(default=False, blank=False, verbose_name='Телевизор ?')
    private_8 = models.BooleanField(default=False, blank=False, verbose_name='Спутниковое TV ?')
    private_9 = models.BooleanField(default=False, blank=False, verbose_name='Барбекю ?')
    private_10 = models.BooleanField(default=False, blank=False, verbose_name='Садовая мебель ?')
    private_11 = models.BooleanField(default=False, blank=False, verbose_name='Офис ?')
    private_12 = models.BooleanField(default=False, blank=False, verbose_name='Камин?')
    private_13 = models.BooleanField(default=False, blank=False, verbose_name='Кинозал?')
    private_14 = models.BooleanField(default=False, blank=False, verbose_name='Сауна ?')
    private_15 = models.BooleanField(default=False, blank=False, verbose_name='Тренажёрный зал ?')
    private_16 = models.BooleanField(default=False, blank=False, verbose_name='Срочно предложения ?')
    private_17 = models.BooleanField(default=False, blank=False, verbose_name='В городе ?')
    private_18 = models.BooleanField(default=False, blank=False, verbose_name='У моря ?')
    private_19 = models.BooleanField(default=False, blank=False, verbose_name='Около подъемника ?')
    private_20 = models.BooleanField(default=False, blank=False, verbose_name='Бассейн ?')
    
    description_1 = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    description_1_en = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском')
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Аренда'

    def __str__(self):
        return f'{self.name} - {self.price_min}'
    

class Sale(models.Model):
    PROPERTY_CHOICES = [
        ('vila', _('Villa')),  
        ('shale', _('Chalet')),  
        ('apartamenti', _('Apartment')),  
        ('yaxta', _('Yacht')), 
    ]
    PROPERTY_CHOICES_2 = [
        ('rent', _('Rent')),  
        ('buy', _('Buy')),  
    ]
    
    Owner_object = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец объекта')
    name = models.CharField(max_length=100, verbose_name='Название')
    name_en = models.CharField(max_length=100, verbose_name='Название на английском')
    description = models.TextField(verbose_name='Информация об объекте')
    description_en = models.TextField(verbose_name='Информация об объекте на английском')
    
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Главная картина')
    img_1 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_2 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_3 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_4 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_5 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_6 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_7 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_8 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_9 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_10 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_11 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_12 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_13 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_14 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_15 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    
    property_type = models.CharField(max_length=15, choices=PROPERTY_CHOICES, verbose_name='тип жилья')
    property_type_2 = models.CharField(max_length=10, choices=PROPERTY_CHOICES_2, default='buy', verbose_name='Аренда или Купить?')
    rooms = models.CharField(max_length=50, blank=True, null=True, verbose_name='Количество спален')
    shower = models.CharField(max_length=50, blank=True, null=True, verbose_name='Количество ванных комнат')
    private_1 = models.BooleanField(default=False, blank=False, verbose_name='Бассейн ?')
    private_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name='До моря')
    price_min = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name='Цена продажи, €')
    square = models.CharField(max_length=50,blank=True, null=True, verbose_name='площадь')
    
    Location = models.CharField(max_length=200, verbose_name='Расположение')
    Location_en = models.CharField(max_length=200, verbose_name='Расположение на английском')
    
    description_1 = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    description_1_en = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском')
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Продажа'

    def __str__(self):
        return f'{self.name} - {self.price_min}'
    

class Yacht(models.Model):
    PROPERTY_CHOICES = [
        ('vila', _('Villa')),  
        ('shale', _('Chalet')),  
        ('apartamenti', _('Apartment')),  
        ('yaxta', _('Yacht')), 
    ]
    PROPERTY_CHOICES_2 = [
        ('rent', _('Rent')),  
        ('buy', _('Buy')),  
    ]
    Owner_object = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец объекта')
    name = models.CharField(max_length=100, verbose_name='Название')
    name_en = models.CharField(max_length=100, verbose_name='Название на английском')
    description = models.TextField(verbose_name='Информация об объекте')
    description_en = models.TextField(verbose_name='Информация об объекте на английском')
    
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Главная картина')
    img_1 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_2 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_3 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_4 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_5 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_6 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_7 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_8 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_9 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_10 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_11 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_12 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_13 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_14 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_15 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    shower_k = models.CharField(max_length=50, blank=True, null=True, verbose_name='Число душевых кабин')
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    
    property_type = models.CharField(max_length=15, choices=PROPERTY_CHOICES, default='yaxta', verbose_name='тип жилья')
    property_type_2 = models.CharField(max_length=10, choices=PROPERTY_CHOICES_2, verbose_name='Аренда или Купить?')
    year = models.CharField(max_length=50, blank=True, null=True, verbose_name='Год выпуска')
    engine = models.CharField(max_length=50, blank=True, null=True, verbose_name='Двигатель')
    long = models.CharField(max_length=50,blank=True, null=True, verbose_name='Длина ')
    price_min = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name='Цена')
    
    Location = models.CharField(max_length=200, verbose_name='Расположение')
    Location_en = models.CharField(max_length=200, verbose_name='Расположение на английском')
    description_1 = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    description_1_en = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском')
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Чартер Яхт'

    def __str__(self):
        return f'{self.name} - {self.price_min}'
    

class News(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название на английском')
    description = models.TextField(blank=True, null=True, verbose_name='Информация об объекте')
    description_en = models.TextField(blank=True, null=True, verbose_name='Информация об объекте на английском')
    
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Главная картина')
    img_1 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_2 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_3 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_4 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_5 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    
    description_1 = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    description_1_en = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация на английском')
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.name} - {self.date_created}'


class Reservation(models.Model):
    arenda = models.ForeignKey(Arenda, on_delete=models.CASCADE, related_name='reservations', verbose_name='объект')
    arrival = models.DateField(verbose_name='Прибытие')
    departure = models.DateField(verbose_name='Выезд')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    preferences = models.TextField(blank=True, null=True, verbose_name='Пожелания')
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = 'Бронирование'

    def __str__(self):
        return f'{self.arenda} - {self.phone}'
    
# Owner_object = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='Владелец объекта')
    
class Applications(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    tel = models.CharField(max_length=60, verbose_name='телефон')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.name} - {self.tel}'
    
    

class Imgmain(models.Model):
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Главная картина')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Шапка главной страницы'

    