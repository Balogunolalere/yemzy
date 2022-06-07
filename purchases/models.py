from django.db import models
from inventory.models import Product, Stock
from phonenumber_field.modelfields import PhoneNumberField


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)    
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'suppliers'


class PurchaseBill(models.Model):
    billno = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return '#' + str(self.billno)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'purchase bills'


class PurchaseItem(models.Model):
    bill = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.IntegerField(default=1)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '#' + str(self.bill.billno)

    class Meta:
        ordering = ['-bill_date']
        verbose_name_plural = 'purchase items'


class Customer(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)    
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'customers'

class SaleBill(models.Model):
    billno = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '#' + str(self.billno) + ' - ' + str(self.customer)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'sale bills'

class SaleItem(models.Model):
    bill = models.ForeignKey(SaleBill, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.IntegerField(default=1)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '#' + str(self.bill.billno) + ' - ' + str(self.stock)

    '''deduct the quantity from the stock'''
    def save(self, *args, **kwargs):
        stock = Stock.objects.get(pk=self.stock.id)
        stock.quantity -= self.total_quantity
        stock.save()
        super(SaleItem, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-bill_date']
        verbose_name_plural = 'sale items'


class SaleReceipt(models.Model):
    bill = models.ForeignKey(SaleBill, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.IntegerField(default=1)
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sales_rep = models.CharField(max_length=200)
    item_description = models.TextField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.name

    class Meta:
        ordering = ['-bill_date']











