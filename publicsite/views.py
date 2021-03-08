from django.shortcuts import render

from .models import MainSliderData, GeneralInfo
from products.models import ProductItem, ProductCategory


def contact(request):
    site_info = GeneralInfo.objects.filter(active=True).first()
    return render(request, 'contact-us.html', {
        'page': 'CONTACT US',
        'contact_active': True,
        'site_info': site_info,
        'footer_categories': ProductCategory.objects.prefetch_related('subcategories').all()[:4]
    })


def index(request):
    slider_data = MainSliderData.objects.all()[:3]
    active_slider = slider_data[0]

    products = ProductItem.objects.all()
    recommend_set_1 = ProductItem.objects.order_by('?')
    recommend_set_2 = ProductItem.objects.order_by('?')

    categories = ProductCategory.objects.prefetch_related('subcategories').all()
    site_info = GeneralInfo.objects.filter(active=True).first()

    return render(request, 'index.html', {
        'page': 'HOME',
        'home_active': True,
        'site_info': site_info,
        'products': products,
        'recommend_products_active': recommend_set_1,
        'recommend_products': recommend_set_2,
        'active_slider': active_slider,
        'slider_items': slider_data[1:],
        'categories': categories,
        'footer_categories': categories[:4]
    })
