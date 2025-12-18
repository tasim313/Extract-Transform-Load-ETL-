from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .migration_table import MigrationTable

class ColumnMapping(BaseModel):
    migration_table = models.ForeignKey(MigrationTable, on_delete=models.CASCADE, related_name='migration_table', null=True, blank=True)
    source_column = models.CharField(max_length=255, verbose_name = "Source Column", related_name="source_column")
    target_column = models.CharField(max_length=255, verbose_name="Target Column", related_name="target_column")
    is_active = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='table_name', unique=True)
    
    def __str__(self):
        return self.source_column + self.target_column