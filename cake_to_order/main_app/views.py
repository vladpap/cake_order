from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Cake, Topping, Berry, Decor, CakeLevel, CakeForm

import io
import base64


# Create your views here.
def index(request):
    toppings = Topping.get_topping()
    cakes = Cake.get_cakes()
    ids = cakes[2]['id']
    img = cakes[2]['img']
    cake = Cake.get_cake(cakes[2]['id'][2])

    buffer = io.BytesIO()
    img = base64.b64encode(buffer.getvalue()).decode('utf8')

    return HttpResponse(f'<h1>СОБРАТЬ СВОЙ АВТОРСКИЙ ТОРТ!</h1> '\
        f'<p>Уровни: {CakeLevel.get_cake_level()}</p>'\
        f'<p>Формы {CakeForm.get_cake_form()}</p>'\
        f'<p>Топпинги: {Topping.get_topping()}</p>'\
        f'<p>Ягоды: {Berry.get_berry()}</p>'\
        f'<p>Декор {Decor.get_decor()}</p>'\
        # f'<p><img src=data:image/png;base64,{img} width="200"></p>'\
        f'<p>Торты: {ids}</p>'\
        f'<p>{cake["text"]}</p>'
        )