from django.shortcuts import render
from .models import ProductItem


def shop(request):
    products = ProductItem.objects.all()

    return render(request, 'shop.html', {
        'page': 'SHOP',
        'shop_active': True,
        'products': products,
    })


def product_detail(request, pk=None):
    current_product = ProductItem.objects.get(id=pk)
    recommend_set_1 = ProductItem.objects.order_by('?')
    recommend_set_2 = ProductItem.objects.order_by('?')
    return render(request, 'product-details.html', {
        'page': 'ITEM-DETAILS',
        'shop_active': True,
        'current_product': current_product,
        'recommend_products_active': recommend_set_1,
        'recommend_products': recommend_set_2,
    })
