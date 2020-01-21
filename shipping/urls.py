from django.urls import path
from . import views

app_name = 'shipping'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
