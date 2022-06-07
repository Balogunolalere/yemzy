import django
from django.contrib import admin

# Register your models here.
from .models import Product, Stock, Category






class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'date_created', 'date_modified')    
    list_filter = ('name', 'price', 'description', 'category', 'date_created', 'date_modified')
    search_fields = ('name', 'price', 'description', 'category', 'date_created', 'date_modified')
    ordering = ['-date_created']
    


class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date_modified')
    list_filter = ('product', 'quantity', 'date_modified')
    search_fields = ('product', 'quantity', 'date_modified')
    ordering = ['-date_modified']


    


admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Category)
