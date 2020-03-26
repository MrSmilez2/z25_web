from django.urls import path

from shop.views import full_list


urlpatterns = [
    path('product', full_list, name='all_products')
]
