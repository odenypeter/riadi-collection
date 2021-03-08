from django.contrib import admin

from .models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'category',)


@admin.register(ProductItem)
class ProductItemAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'specifications')
    list_display = (
        'product_uuid',
        'name',
        'price',
        'category',
        'subcategory',
        'in_stock'
    )
    list_filter = ('category', 'subcategory', 'in_stock')
    search_fields = ('name',)

