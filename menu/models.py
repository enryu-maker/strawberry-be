from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Category name'))
# Create your models here.


class MenuItem(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(_("image"), upload_to=None)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
