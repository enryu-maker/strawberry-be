"""
Author: Ritesh Mahale
Module: Models
Description: Custom User Model
Last Updated: 25 Aug 2024
"""


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Change the default User Model beahavier to login with 'email'.
    """
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(
        'Designates whether the user can log into this admin site')
    )

    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. Unselect this instead of deleting account')
    )

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    is_trusty = models.BooleanField(_('trusty'), default=False, help_text=_(
        'Designates whether this user has confirmed his account.')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return self.name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'user'


class Vendor(User):
    """
    Vendor Model
    """
    pass


class Customer(User):
    """
    Customer Model
    """
    pass
