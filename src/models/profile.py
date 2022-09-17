from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='profile',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    easy = models.IntegerField(_('Easy'), validators=[MinValueValidator(0)])
    medium = models.IntegerField(_('Medium'), validators=[MinValueValidator(0)])
    hard = models.IntegerField(_('Hard'), validators=[MinValueValidator(0)])
    streak = models.IntegerField(_('Streak'), validators=[MinValueValidator(0)], default=0)
    last_solved_date = models.DateTimeField(_('Last solved date'), null=True)
    photo = models.ImageField(_('Photo'), null=True, blank=True)
    rating = models.IntegerField(_('Rating'), validators=[MinValueValidator(0)])

    def __str__(self):
        return self.user.leetcode_username
