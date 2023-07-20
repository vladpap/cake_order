from django.contrib import admin
from .models import Client, Cake, Topping, Berry, Decor, CakeLevel, CakeForm


admin.site.register(Client)
admin.site.register(Cake)
admin.site.register(Topping)
admin.site.register(Berry)
admin.site.register(Decor)
admin.site.register(CakeLevel)
admin.site.register(CakeForm)

# Register your models here.
