from django.db import models
from shop.models import Product


class Order(models.Model):
    SHIPPING_CHOICES = (
        ('1', 'Free shipping +0.0$'),
        ('2', 'Express shipping +9.99$'),
        ('3', 'Courier shipping +19.99$'),
        ('4', 'Free Express shipping'),
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    shipping_options = models.CharField(max_length=100, choices=SHIPPING_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
