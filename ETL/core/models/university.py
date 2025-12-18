from django.db import models
from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField
class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)
    logo = VersatileImageField(
        'University Logo',
        upload_to='universities/logos/',
        blank=True,
        null=True
    )
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name