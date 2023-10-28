from django.contrib import admin

from .models import Client, Dish, Order, OrderItem

admin.site.register(Client)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(OrderItem)
