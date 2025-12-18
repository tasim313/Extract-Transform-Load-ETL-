from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .user import User

class ProviderType(models.TextChoices):
    GITHUB = 'github', 'GitHub'
    GITLAB = 'gitlab', 'GitLab'

class VersionControlProvider(BaseModel):
    git_username = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name="Git Username", related_name='git_user_name')
    provider_type = models.CharField(max_length=255, choices=ProviderType.choices, default=ProviderType.GITHUB)
    slug = AutoSlugField(populate_from='git_username', unique=True)
    base_url = models.URLField(blank=True, null=True, verbose_name="Base Url", related_name='base_url', help_text='Enter the API base URL, e.g., "https://gitlab.company.com/api/v4"')
    git_access_token = models.CharField(max_length=255, blank=True, null=True)
    commit_author_name = models.CharField(max_length=255, blank=True, null=True)
    commit_author_email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.git_username