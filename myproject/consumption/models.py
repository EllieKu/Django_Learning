from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class Retailer(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("name"))
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("retailer")
        verbose_name_plural = _("retailers")


class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name=_("name"))
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Commodity(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("name"))
    spec = models.CharField(max_length=20, verbose_name=_("spec"), default="", blank=True)
    brand = models.CharField(max_length=20, verbose_name=_("brand"))
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}_{self.brand}_{self.spec}"

    class Meta:
        verbose_name = _("commodity")
        verbose_name_plural = _("commodities")

class Transaction(models.Model):
    commodity = models.ForeignKey( Commodity, verbose_name=_("commodity"), on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name=_("quantity"))
    cost = models.IntegerField(verbose_name=_("cost"), validators=[MinValueValidator(1)])
    retailer = models.ForeignKey(Retailer, verbose_name=_("retailer"), on_delete=models.PROTECT)
    note = models.CharField(max_length=50, verbose_name=_("note"), null=True, blank=True)
    date = models.DateField(verbose_name=_("date"))

    @property
    def unit_price(self):
        if self.quantity:
            return round(self.cost / self.quantity, 1)
        return None

    def __str__(self):
        return f"{self.date} {self.commodity}"

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")
