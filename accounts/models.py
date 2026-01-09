from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    REPORTER = 'reporter'
    EDITOR = 'editor'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (REPORTER, 'Reporter'),
        (EDITOR, 'Editor'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=REPORTER,
    )