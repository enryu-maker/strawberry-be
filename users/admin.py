from django.contrib import admin
from .models import User, Vendor, Customer
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    User Admin to register User Model
    """

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_trusty', 'is_staff',
                                       'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff'),
        }),
    )
    list_display = ('id', 'email', 'name', 'is_staff')
    list_display_links = ('id', 'email', 'name')
    search_fields = ('email', 'name')
    ordering = ('id', 'email')


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_trusty', 'is_staff',
                                       'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff'),
        }),
    )
    list_display = ('id', 'email', 'name', 'is_staff')
    list_display_links = ('id', 'email', 'name')
    search_fields = ('email', 'name')
    ordering = ('id', 'email')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
