from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    birth_Day = models.DateField(null = True)
    deleted = models.BooleanField(default = False)

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()