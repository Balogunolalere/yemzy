from django.contrib import admin
from .models import Supplier, Customer, PurchaseBill, PurchaseItem, SaleBill, SaleItem, SaleReceipt
# Register your models here.


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'date_created',)
    list_filter = ('name', 'phone_number', 'email', 'date_created', )
    search_fields = ('name', 'phone_number', 'email', 'date_created', )
    ordering = ['-date_created']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'date_created', )
    list_filter = ('name', 'phone_number', 'email', 'date_created', )
    search_fields = ('name', 'phone_number', 'email', 'date_created',)
    ordering = ['-date_created']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(SaleBill)
admin.site.register(SaleItem)
admin.site.register(SaleReceipt)
