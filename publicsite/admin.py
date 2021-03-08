from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


@admin.register(MainSliderData)
class MainSliderDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')


@admin.register(PolicyTerm)
class PolicyTermAdmin(SummernoteModelAdmin):
    summernote_fields = ('terms_of_use', 'privacy_policy', 'refund_policy')
    list_display = ('create_date', 'edited_date', 'id')


@admin.register(PublicMessage)
class PublicMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender_email', 'received_at', 'read')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol')


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = (
        'email_address',
        'phone_number',
        'street_name',
        'zip_code',
        'city',
        'currency',
        'active'
    )
