#from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Product, Stock, Category

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class StockList(ListView):
    model = Stock
    template_name = 'stock_list.html'
    context_object_name = 'stocks'

class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'



