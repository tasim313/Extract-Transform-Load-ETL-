from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .etl_database_profile import ETLDatabaseProfile

class DatabaseSchema(BaseModel):
    db_profile = models.ForeignKey(ETLDatabaseProfile, on_delete=models.CASCADE, related_name='database_profile', null=True, blank=True)
    schema_name = models.CharField(max_length=255, verbose_name = "Database Schema Name", related_name="schema_name")
    slug = AutoSlugField(populate_from='name', unique=True)
    
    def __str__(self):
        return self.schema_name