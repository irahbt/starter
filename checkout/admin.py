from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'first_name',
              'last_name',  'email', 'phone_number',
              'street_address1', 'street_address2',
              'town_or_city', 'county', 'country', 'postcode',
              'shipping_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'shipping_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)