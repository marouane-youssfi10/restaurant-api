import uuid
import typing

from django.utils.html import format_html
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core_apps.core.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(
        verbose_name=_("username"), db_index=True, max_length=255, unique=True
    )
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)
    email = models.EmailField(
        verbose_name=_("email address"), db_index=True, unique=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), upload_to="photos/profile_photo", blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> typing.Text:
        return self.username

    @property
    def get_full_name(self) -> typing.Text:
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> typing.Text:
        return self.first_name

    def display_picture(self):
        html = '<img src="{}" width="170px;">'
        if self.profile_photo:
            return format_html(html, self.profile_photo.url)
        return format_html("<strong>There is no picture for this user.<strong>")

    display_picture.short_description = "Picture preview"
