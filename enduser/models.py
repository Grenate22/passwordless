from uuid  import uuid4
import random
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.validators import EmailValidator
from datetime import datetime, timedelta
from .utils import generate_pin

# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=50,blank=True,null=True,unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)


class Pin(models.Model):
    email = models.EmailField(max_length=50)
    otp = models.CharField(max_length=6)
    otp_expiry = models.DateTimeField(blank=True, null=True, default=timezone.now()+timedelta(minutes=10))
    max_otp_try = models.PositiveSmallIntegerField(default=settings.MAX_OTP_TRY)
    created_at = models.DateTimeField(auto_now_add=True)
    attempt_count = models.PositiveIntegerField(default=0)

    def generate_save_pin(self):
        self.otp = generate_pin()
        self.attempt_count = 0
        self.save()

    def __str__(self) -> str:
        return f"self.email"

    