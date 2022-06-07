from django.urls import path
from .views import ProductDetail, ProductList, StockList, CategoryList

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('categories/', CategoryList.as_view(), name='product_categories'),
    path('stocks/', StockList.as_view(), name='product_stocks'),
]