from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ClientUser(models.Model):
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
        blank=True,
        db_index=True)


    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'