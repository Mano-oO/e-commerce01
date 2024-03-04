# your_app_name/admin.site.py
from django.contrib import admin
from .models import Cart, Page, Category, Product, Banner, CartItem, Order, OrderItem

admin.site.register(Cart)


admin.site.register(Page)


admin.site.register(Category)


admin.site.register(Product)


admin.site.register(Banner)


admin.site.register(CartItem)


admin.site.register(Order)


admin.site.register(OrderItem)
