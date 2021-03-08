from django.urls import path
from .views import (index, contact, terms_and_conditions)

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('<slug:policy>', terms_and_conditions, name='policy')
]