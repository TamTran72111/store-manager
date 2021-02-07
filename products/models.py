from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    product = models.ForeignKey(Product,
                                related_name="units",
                                related_query_name='unit',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} | {self.name}'
