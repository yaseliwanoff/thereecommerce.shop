from django.contrib import admin
from app.models import Product,Customer, Cart


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']


# @admin.register(Cart)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'products', 'quantity']
