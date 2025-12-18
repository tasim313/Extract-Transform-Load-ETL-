from django.db import models
from .company import Company
from autoslug import AutoSlugField

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='teams',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name