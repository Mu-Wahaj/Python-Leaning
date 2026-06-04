from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # Display these fields in the admin list view

class OfferAdmin(admin.ModelAdmin):
    list_display = ('discount_code','discount_percentage')  # Display these fields in the admin list view


admin.site.register(Product, ProductAdmin)  # Register the Product model with the custom ProductAdmin configuration
admin.site.register(Offer, OfferAdmin)  # Register the Offer model with the custom OfferAdmin   configuration