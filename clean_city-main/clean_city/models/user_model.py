from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import CustomUserManager


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password_changed = models.BooleanField(default=False)
    sex = models.CharField(max_length=50, null=True)
    otp = models.CharField(null=True, max_length=6)
    profile_image = models.URLField(null=True)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_cleaner = models.BooleanField(default=False)
    is_bin_collector = models.BooleanField(default=False)

    def user_type(self):
        group = ("manager" if self.is_manager
                 else "cleaner" if self.is_cleaner
                 else "garbage collector" if self.is_bin_collector
                 else "admin")
        return group

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ["-created_at"]
