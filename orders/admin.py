from django.contrib import admin

from .models import Order, OrderDetail

admin.site.register(OrderDetail)


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display = ('customer', 'created_at', 'total')
