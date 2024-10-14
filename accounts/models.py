from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# Create your models here.


class User(AbstractUser):
    """This enalbles the user to siginusing password and email"""
    id = models.UUIDField(default=uuid4, unique=True,
                          primary_key=True, editable=True)
    email = models.EmailField(unique=True)

    # username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email
