from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Product
from cart.forms import CartAddProductForm
from .utils import load_to_bd


def product_list(request):
    """
    Функция отображения списка товаров.
    """
    products = Product.objects.filter(available=True)
    paginator=Paginator(products, 9)
    page_number=request.GET.get('page', 1)
    page=paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/list.html',
                  {'products': page,
                  'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    """
    Функция отображения детальной информации о товаре.
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def load_data(request):
    """
    Функция загрузки данных с .json файла в BD
    """
    load_to_bd()
    return redirect('shop:product_list')
