from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User


# Register your models here.



admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)