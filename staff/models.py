from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name
