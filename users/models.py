import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_uuid = models.CharField(unique=True, default=uuid.uuid4, max_length=100, db_index=True)

    def __str__(self):
        return self.username
