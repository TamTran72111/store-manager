from django.contrib import admin

from .models import Product, Unit


class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [UnitInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Unit)
