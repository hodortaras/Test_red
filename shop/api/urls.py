from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDestroyView


app_name = 'api'

urlpatterns = [
    path('products/',  ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/destroy/<pk>/', ProductDestroyView.as_view(), name='product_destroy'),
    path('products/<pk>/', ProductDetailView.as_view(), name='product_detail'),
]
