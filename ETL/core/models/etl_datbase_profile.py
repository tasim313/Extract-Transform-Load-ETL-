from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel

class ETLDatabaseProfile(BaseModel):
    profile_name = models.CharField(max_length=255, verbose_name = "Name", related_name="profile_name")
    slug = AutoSlugField(populate_from='profile_name', unique=True)
    db_engine = models.CharField(max_length=255, verbose_name = "Database Engine", related_name="db_engine")
    db_host = models.CharField(max_length=255, verbose_name="Database Host", related_name="db_host")
    db_port = models.CharField(max_length=255, verbose_name="Database Port", related_name="db_port")
    db_username = models.CharField(max_length=255, verbose_name="Database Username", related_name="db_user_name")
    db_password = models.CharField(max_length=255, verbose_name="Database Password", related_name="db_password")
    db_name = models.CharField(max_length=255, verbose_name="Database Name", related_name="db_name")
   
    def __str__(self):
        return self.profile_name