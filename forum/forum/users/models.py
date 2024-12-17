from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass  # Здесь можно добавлять дополнительные поля для пользователя.
