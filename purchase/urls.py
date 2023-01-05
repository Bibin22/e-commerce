from django.urls import path
from .views import *
urlpatterns = [
    path('home', home, name='home'),
    path('cart_items', cart_items, name='cart_items'),
    path('cart/<str:pk>', cart, name='cart'),
    path('remove_from/<str:pk>', remove_from, name='remove_from'),
    path('cart_plus/<str:pk>', cart_plus, name='cart_plus'),
    path('cart_minus/<str:pk>', cart_minus, name='cart_minus'),

    path('payment_add/<str:pk>', payment_add, name='payment_add'),
    path('payment-status/<str:pk>', payment_status, name='payment-status'),
    path('download_invoice/<str:pk>', download_invoice, name='download_invoice')
]