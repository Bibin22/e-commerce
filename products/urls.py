from django.urls import path
from .views import *
urlpatterns = [

    path('', product_list, name='product_list'),
    path('product_add', product_add, name='product_add'),
    path('product_details/<int:pk>', product_details, name='product_details'),
    path('product_delete/<int:pk>', product_delete, name='product_delete'),
    path('product_edit/<int:pk>', product_edit, name='product_edit')
]