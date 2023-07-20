from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Клиент')

    telegram_id = models.CharField(
        'Telegram id',
        max_length=50,
        db_index=True)

    phone = PhoneNumberField(
        'Номер телефона',
        null=True,
        blank=True)
    adress = models.CharField(
        'Адрес',
        max_length=50,
        null=True,
        blank=True)


    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Cake(models.Model):
    title = models.CharField(
        'Название',
        max_length=50)
    description = models.TextField(
        'Описание',)
    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)
    weight = models.DecimalField(
        'Вес',
        max_digits=4,
        decimal_places=2)
    image = models.ImageField(
        'Картинка',
        upload_to='cakes_img')


    class Meta:
        verbose_name='Торт'
        verbose_name_plural='Торты'


    def __str__(self):
        return f'{self.title}, {self.weight} кг., {self.price} р.'


class Topping(models.Model):
    title = models.CharField(
        'Название',
        max_length=50)
    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)


    class Meta:
        verbose_name='Топпинг'
        verbose_name_plural='Топпинги'


    def __str__(self):
        return f'{self.title}, {self.price} р.'


    def get_topping():
        base = Topping.objects.all()
        toppings = {}
        for record in base:
            toppings[record.id] = f'{record.title} (+ {record.price} р.)'

        return toppings



class Berry(models.Model):
    title = models.CharField(
        'Название',
        max_length=50)
    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)


    class Meta:
        verbose_name='Ягода'
        verbose_name_plural='Ягоды'


    def __str__(self):
        return f'{self.title}, {self.price} р.'

    def get_berry():
        base = Berry.objects.all()
        berrys = {}
        for record in base:
            berrys[record.id] = f'{record.title} (+ {record.price} р.)'

        return berrys


class Decor(models.Model):
    title = models.CharField(
        'Название',
        max_length=50)
    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)


    class Meta:
        verbose_name='Декор'
        verbose_name_plural='Декор'


    def __str__(self):
        return f'{self.title}, {self.price} р.'


    def get_decor():
        base = Decor.objects.all()
        decors = {}
        for record in base:
            decors[record.id] = f'{record.title} (+ {record.price} р.)'

        return decors


class CakeLevel(models.Model):
    title = models.CharField(
        'Название',
        max_length=50)
    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)


    class Meta:
        verbose_name='Уровень'
        verbose_name_plural='Уровни'


    def __str__(self):
        return f'{self.title}, {self.price} р.'


    def get_cake_level():
        base = Decor.objects.all()
        cake_levels = {}
        for record in base:
            cake_levels[record.id] = f'{record.title} (+ {record.price} р.)'

        return cake_levels


class CakeForm(models.Model):
    title = models.CharField(
        'Название',
        max_length=50)
    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)


    class Meta:
        verbose_name='Форма'
        verbose_name_plural='Формы'


    def __str__(self):
        return f'{self.title}, {self.price} р.'


    def get_cake_form():
        base = Decor.objects.all()
        cake_form = {}
        for record in base:
            cake_form[record.id] = f'{record.title} (+ {record.price} р.)'

        return cake_form
