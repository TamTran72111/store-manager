from django.db import models
from django.db.models.signals import pre_save

from utils.mixins import SearchNameMixin


class Customer(models.Model, SearchNameMixin):
    name = models.CharField(max_length=200)
    search_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=256, blank=True)
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def update_order_detail(self, new_cost, old_cost=0):
        if old_cost != new_cost:
            self.debt += new_cost - old_cost
            self.save()

    def pay(self, payment):
        if payment != 0:
            self.debt -= payment
            self.save()


pre_save.connect(Customer.pre_save, Customer, dispatch_uid='Customer_pre_save')
