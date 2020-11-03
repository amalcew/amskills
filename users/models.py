from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    number = models.CharField(_('number'), max_length=9, blank=True)
    show_number = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='static/images', blank=True)
    about_me = models.TextField(blank=True)
    social_media = models.CharField(_('social media'), max_length=200, blank=True)
    show_social_media = models.BooleanField(default=False)
    repository = models.CharField(_('repository'), max_length=200, blank=True)
    show_repository = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_pseudonym(self):
        """
        Returns the pseudonym for the user - First letter of the name and surname, for example pseudonym of Bob Moses
        be 'bmoses'
        """
        pseudonym = ('%.1s%s' % (self.first_name, self.last_name))
        return pseudonym.lower()

    def __str__(self):
        return self.email
