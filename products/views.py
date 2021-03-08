from django.db.models import Q
from django.shortcuts import render

from publicsite.models import GeneralInfo
from .models import ProductItem, ProductCategory


def shop(request):
    # get query strings
    category = request.GET.get('category', 0)
    subcategory = request.GET.get('subcategory', 0)
    products = ProductItem.objects.all()

    if category != 0 or subcategory != 0:
        try:
            products = products.filter(
                Q(category__id=int(category)) |
                Q(subcategory__id=int(subcategory))
            )
        except ValueError:
            pass

    categories = ProductCategory.objects.prefetch_related('subcategories').all()
    site_info = GeneralInfo.objects.filter(active=True).first()

    return render(request, 'shop.html', {
        'page': 'SHOP',
        'shop_active': True,
        'products': products,
        'categories': categories,
        'footer_categories': categories[:4],
        'site_info': site_info
    })


def product_detail(request, pk=None):
    current_product = ProductItem.objects.get(id=pk)
    recommend_set_1 = ProductItem.objects.order_by('?')
    recommend_set_2 = ProductItem.objects.order_by('?')

    categories = ProductCategory.objects.prefetch_related('subcategories').all()
    site_info = GeneralInfo.objects.filter(active=True).first()

    return render(request, 'product-details.html', {
        'page': 'ITEM-DETAILS',
        'shop_active': True,
        'current_product': current_product,
        'recommend_products_active': recommend_set_1,
        'recommend_products': recommend_set_2,
        'categories': categories,
        'site_info': site_info,
        'footer_categories': categories[:4]
    })
