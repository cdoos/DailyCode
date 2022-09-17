from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, leetcode_username, password, **extra_fields):
        if not leetcode_username:
            raise ValueError(_('The leetcode_username must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, leetcode_username=leetcode_username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, leetcode_username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, leetcode_username, password, **extra_fields)