import os

from aiogram import Bot, Dispatcher


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cake_to_order.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

import django
from django.conf import settings

if not settings.configured:
    django.setup()

from cake_to_order.settings import TG_BOT_TOKEN
from main_app.models import ClientUser


def main():
    print(TG_BOT_TOKEN)

if __name__ == '__main__':
    main()