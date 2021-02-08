from django.db import models
from django.db.models.signals import pre_save

from utils.mixins import SearchNameMixin


class Product(models.Model, SearchNameMixin):
    name = models.CharField(max_length=200)
    search_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


pre_save.connect(Product.pre_save, Product, dispatch_uid='Product_pre_save')


class Unit(models.Model):
    product = models.ForeignKey(Product,
                                related_name="units",
                                related_query_name='unit',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} | {self.name}'
