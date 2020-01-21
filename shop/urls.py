from django.urls import path
from .views import product_list, product_detail, load_data


app_name = 'shop'

urlpatterns = [
    path('',  product_list, name='product_list'),
    path('load/',load_data, name='load_data'),
    path('product_detail/<id>/<slug>', product_detail, name='product_detail'),
]
