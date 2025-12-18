from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .user import User
from .version_control_provider import VersionControlProvider

class VersionControlRepository(BaseModel):
    provider = models.ForeignKey(VersionControlProvider,
        on_delete=models.CASCADE,
        related_name='Version Control Provider',
        null=True,
        blank=True)
    owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='repositories',
        null=True,
        blank=True)
    repository_name = models.CharField(max_length=255, verbose_name = "Repository Name", related_name="repository_name")
    repository_url = models.URLField(blank=True, null=True, verbose_name="Repository Url", related_name='repository_url', help_text='Enter the repository URL, e.g., "git@github.com:tasim313/Daily-Routine-Plan.git"')
    slug = AutoSlugField(populate_from='name', unique=True)
    default_branch = models.CharField(max_length=255, blank=True, null=True)
    is_auto_created = models.BooleanField(default=False)
    
   
    def __str__(self):
        return self.repository_name