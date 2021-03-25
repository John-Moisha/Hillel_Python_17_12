import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def user_upload_avatar(instance, filename):
    path = f'avatars/{instance.id}/{filename}'
    return path


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True,
    )


    def save(self, *args, **kwargs):

        if not self.username:
            self.username = str(uuid.uuid4())

        super().save(*args, **kwargs)


class ContactUs(models.Model):
    full_name = models.CharField(max_length=128)
    contact_to_email = models.EmailField()
    message = models.CharField(max_length=1024)
    created = models.DateField(auto_now_add=True)
    # message = models.TextField()
