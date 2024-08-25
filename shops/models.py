"""
Author: Ritesh Mahale
Module: Models
Description: Shop Models
Last Updated: 25 Aug 2024
"""


from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    """
    Shop model for vendor
    """
    owner = models.ForeignKey(
        "users.Vendor", verbose_name=_("Owner"), on_delete=models.CASCADE, related_name="owner"
    )
    name = models.CharField(_("Name"), max_length=100, null=True)
    description = models.TextField(_("Description"), null=True)
    address = models.TextField(_("Address"), null=True)
    phone_number = models.CharField(
        _("Mobile Number"), max_length=50, null=True)
    icon = models.ImageField(_("Icon"), upload_to='shop/icon', null=True)


class ShopImages(models.Model):
    """
    Multiple Images for shop
    """
    image = models.ImageField(_("Shop Image"), upload_to="shop/images")
    shop = models.ForeignKey(
        Shop, verbose_name=_("Shop"), on_delete=models.CASCADE, related_name="shop_images"
    )
