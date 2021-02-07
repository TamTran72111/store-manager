from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=256, blank=True)
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.name
