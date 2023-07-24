from django.contrib import admin
from django.utils import timezone
from datetime import datetime
from .models import Client, Cake, Topping, Berry, Decor, CakeLevel, CakeForm, OrderCake


admin.site.register(Client)
admin.site.register(Cake)
admin.site.register(Topping)
admin.site.register(Berry)
admin.site.register(Decor)
admin.site.register(CakeLevel)
admin.site.register(CakeForm)
# admin.site.register(OrderCake)

# Register your models here.
@admin.register(OrderCake)
class OrderCakeAdmin(admin.ModelAdmin):
    list_display = [
        'get_client_full_name',
        'get_create_at',
        'get_cake',
        'get_topping',
        'get_berry',
        'get_decor',
        'inscription',
        'comment',
        'get_order_date',
        'get_order_time',
        'phone',
        'adress',
        'get_amount',
        ]
    # list_filter = ['is_speaker',]
    # search_fields = ('user__email',
    #                  'user__first_name',
    #                  'user__last_name',
    #                  'phone')

    def get_topping(self, obj):
        return obj.topping.title if obj.topping else '-'

    get_topping.short_description = 'Топпинг'


    def get_berry(self, obj):
        return obj.berry.title if obj.berry else '-'

    get_berry.short_description = 'Ягоды'


    def get_decor(self, obj):
        return obj.decor.title if obj.decor else '-'

    get_decor.short_description = 'Декор'


    def get_create_at(self, obj):
        return obj.create_at.strftime('%d.%m.%y %H:%M')

    get_create_at.short_description = 'Заказано'


    def get_client_full_name(self, obj):
        return f'{obj.client.user.first_name} {obj.client.user.last_name}'

    get_client_full_name.short_description = 'Клиент'


    def get_cake(self, obj):
        if obj.cake_catalog:
            cake_str = obj.cake_catalog.title
        else:
            cake_str = f'{obj.cake_form.title}, {obj.cake_level.title}'

        return cake_str

    get_cake.short_description = 'Торт'


    def get_order_date(self, obj):
        return obj.order_date.strftime('%d.%m')

    get_order_date.short_description = 'Доставка'


    def get_order_time(self, obj):
        return obj.order_time

    get_order_time.short_description = 'Время'


    def get_amount(self, obj):
        amount = 0
        amount += obj.cake_catalog.price if obj.cake_catalog else 0
        amount += obj.cake_level.price if obj.cake_level else 0
        amount += obj.cake_form.price if obj.cake_form else 0
        amount += obj.topping.price if obj.topping else 0
        amount += obj.berry.price if obj.berry else 0
        amount += obj.decor.price if obj.decor else 0
        amount += 500 if obj.inscription else 0
        return f'{amount} ₽'

    get_amount.short_description = 'Сумма'
