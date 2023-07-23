from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Cake, Topping, Berry, Decor, CakeLevel, CakeForm, OrderCake

import io
import base64


# Create your views here.
def index(request):
    record1 = OrderCake.save_order(
        {
        'page': 1, 
        'cake_id': '12', 
        'shape_id': 'no_data', 
        'topping_id': '1', 
        'berry_id': 'no_data', 
        'decor_id': '6', 
        'inscription': 'Дорогой!', 
        'comment': 'Комментарий', 
        'name': 'Владимир', 
        'phone': '+79999999999', 
        'address': 'Адрес доставки', 
        'date': '26.07', 
        'time': '11:00 - 15:00', 
        'telegram_id': 192419599, 
        'level_id': 'no_data'
        })
    return HttpResponse(f'<h1>СОБРАТЬ СВОЙ АВТОРСКИЙ ТОРТ!</h1> '\
        # f'<img src="../pictures/Tort.png" >'
        f'Client: {Client.get_client("234")}'\
        f'<p>{record1}</p>'
        )