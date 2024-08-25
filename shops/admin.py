from django.contrib import admin
from .models import Shop, ShopImages
# Register your models here.


class ShopImagesInline(admin.StackedInline):
    """
    Shop Images Inline to add images from Shop admin
    """
    model = ShopImages
    extra = 1


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    """
    Shop Admin registration on django admin
    """
    inlines = [ShopImagesInline,]


@admin.register(ShopImages)
class ShopImagesAdmin(admin.ModelAdmin):
    """
    Shop Images Admin registration on django admin
    """
    pass
