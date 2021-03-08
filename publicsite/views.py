from django.shortcuts import render

from .models import MainSliderData
from products.models import ProductItem


def contact(request):
    return render(request, 'contact-us.html', {
        'page': 'CONTACT US',
        'contact_active': True
    })


def index(request):
    slider_data = MainSliderData.objects.all()[:3]
    active_slider = slider_data[0]

    products = ProductItem.objects.all()
    recommend_set_1 = ProductItem.objects.order_by('?')
    recommend_set_2 = ProductItem.objects.order_by('?')

    return render(request, 'index.html', {
        'page': 'HOME',
        'home_active': True,
        'products': products,
        'recommend_products_active': recommend_set_1,
        'recommend_products': recommend_set_2,
        'active_slider': active_slider,
        'slider_items': slider_data[1:]
    })
