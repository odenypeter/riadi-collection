from django.urls import path
from .views import (product_detail, shop)

urlpatterns = [
    path('', shop, name='shop'),
    path('<int:pk>', product_detail, name='product-detail'),
]
