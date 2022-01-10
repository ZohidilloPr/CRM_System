from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse

from .menegers import CustomUserManeger
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(("ISM"), max_length=50)
    last_name = models.CharField(("FAMILYA"), max_length=50)
    address = models.CharField(("MANZIL"), max_length=250)
    img = models.ImageField(("Profile uchun Rasm"), upload_to='user_pic/', null=True, blank=True)
    email = models.EmailField(('EMAIL'), unique=True)
    phone_number = models.CharField(('TELEFON RAQAM'), max_length=9)
    joined_date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse("accounts:RGU", kwargs={"pk": self.pk})

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_superuser

    objects = CustomUserManeger()