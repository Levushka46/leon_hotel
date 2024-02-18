from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class City(models.Model):
    name = models.CharField(_("city name"), max_length=150, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")


class Hotel(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?7?\d{10}$", message="Phone number must be entered in the format: '+799999999'. 10 digits allowed."
    )

    name = models.CharField(_("name"), max_length=150, blank=False)
    address = models.CharField(_("address"), max_length=150, blank=False)
    phone = models.CharField(_("phone"), validators=[phone_regex], max_length=12, blank=True)
    city = models.ForeignKey(City, verbose_name=_("city name"), on_delete=models.CASCADE, related_name="city")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("hotel")
        verbose_name_plural = _("hotels")
