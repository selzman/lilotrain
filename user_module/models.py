from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
