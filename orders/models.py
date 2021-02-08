from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import datetime

from customers.models import Customer
from products.models import Unit


class Order(models.Model):
    ORDER_STATUS = (
        ('o', 'Ordered'),
        ('p', 'Preparing'),
        ('r', 'Ready'),
        ('s', 'Shipped'),
    )

    customer = models.ForeignKey(
        Customer,
        related_name='orders',
        related_query_name='order',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='o'
    )
    debt = models.DecimalField(default=0, max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.customer.name} - ' +\
            f'{self.created_at.strftime("%b %d %Y %H:%M:%S")}'

    @property
    def total(self):
        return sum([detail.cost for detail in self.details.all()])

    def is_shipped(self):
        return self.status == 's'

    @classmethod
    def get_query_orders(cls, query):
        time_query = query.get('time')
        if time_query == 'today':
            today = datetime.datetime.today() - datetime.timedelta(hours=4)
            return Order.objects.filter(created_at__gte=today)
        return Order.objects.order_by('-created_at')


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='details',
        related_query_name='detail',
        on_delete=models.CASCADE
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # Need to have a price to avoid the effect of changing price in unit
    price = models.DecimalField(
        blank=True, default=0, max_digits=15, decimal_places=2)
    ready = models.BooleanField(default=False)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(
        blank=True, default=0, max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} ::: {self.order}'

    @property
    def product(self):
        return self.unit.product

    @property
    def cost(self):
        return self.price * self.quantity

    def update_price(self):
        self.price = self.unit.price

    def is_shipped(self):
        return self.order.is_shipped()


@receiver(pre_save, sender=OrderDetail, dispatch_uid='OrderDetail_pre_save')
def get_price(sender, instance, *args, **kwargs):
    instance.update_price()
