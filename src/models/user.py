from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework.validators import ValidationError
from .profile import Profile
from src.managers import CustomUserManager
from external_api.leetcode import get_solved_problems, get_last_submission_date


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=30, unique=True)
    leetcode_username = models.CharField(_("Leetcode username"), max_length=30, unique=True)
    password = models.CharField(_("password"), max_length=30)
    is_staff = models.BooleanField(_('Admin'), default=False)

    USERNAME_FIELD = 'leetcode_username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        try:
            data = get_solved_problems(self.leetcode_username)
            data['last_solved_date'] = get_last_submission_date(self.leetcode_username)
        except ValueError as e:
            raise ValidationError(e)
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            data['user'] = self
            data['rating'] = data['hard'] * 7 + data['medium'] * 3 + data['easy'] * 1
            Profile.objects.create(
                user=data['user'],
                easy=data['easy'],
                medium=data['medium'],
                hard=data['hard'],
                last_solved_date=data['last_solved_date'],
                rating=data['rating']
            )

    def __str__(self):
        return self.leetcode_username
