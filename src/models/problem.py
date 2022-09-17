from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Problem(models.Model):

    class Type(models.TextChoices):
        EASY = 'Easy', _('Easy')
        MEDIUM = 'Medium', _('Medium')
        HARD = 'Hard', _('Hard')

    problem_id = models.IntegerField(_('Problem ID'), validators=[MinValueValidator(1), MaxValueValidator(5000)])
    title = models.CharField(_('Title'), max_length=300)
    titleSlug = models.CharField(_('Title Slug'), max_length=300)
    type = models.CharField(_('Type'), max_length=6, choices=Type.choices)
    solved = models.BooleanField(_('Solved'), default=False)
    profile = models.ForeignKey(
        'src.Profile',
        verbose_name=_('Profile'),
        related_name='problems',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (('profile', 'problem_id'), )

    def __str__(self):
        return self.title
