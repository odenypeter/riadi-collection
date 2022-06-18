import uuid

from django.db import models


class ProductCategory(models.Model):
    category = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category


class ProductSubcategory(models.Model):
    subcategory = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(ProductCategory, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory


class ProductItem(models.Model):
    product_uuid = models.CharField(unique=True, default=uuid.uuid4, max_length=100, db_index=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    specifications = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    promotion_price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=20)
    preview_image = models.ImageField(
        upload_to='uploads',
        null=True, blank=True,
        help_text='Image Size should be 268x249'
    )
    main_image = models.ImageField(
        upload_to='uploads',
        null=True, blank=True,
        help_text='Image Size should be 266x381'
    )
    recommend_image = models.ImageField(
        upload_to='uploads',
        null=True, blank=True,
        help_text='Image Size should be 268x134'
    )
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(ProductSubcategory, null=True, blank=True, on_delete=models.SET_NULL)

    added_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
