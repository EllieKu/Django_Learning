from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Transaction, Category, Retailer, Commodity

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["commodity_name", "commodity_brand", "commodity_spec", "quantity", "cost", "unit_price", "date"]
    list_filter = ["commodity", "date"]
    search_fields = ["commodity__name", "commodity__brand"]
    list_select_related = ["commodity", "retailer"]

    @admin.display(description=_("name"))
    def commodity_name(self, obj):
        return obj.commodity.name

    @admin.display(description=_("brand"))
    def commodity_brand(self, obj):
        return obj.commodity.brand

    @admin.display(description=_("spec"))
    def commodity_spec(self, obj):
        return obj.commodity.spec

    @admin.display(description=_("unit price"))
    def unit_price(self, obj):
        return obj.unit_price




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ["name", "spec", "brand"]
    search_fields = ["name", "spec"]
    list_select_related = ["category"]
