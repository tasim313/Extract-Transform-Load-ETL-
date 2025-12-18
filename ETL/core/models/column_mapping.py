from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .migration_table import MigrationTable

class ColumnMetaData(BaseModel):
    table = models.ForeignKey(TableMetaData, on_delete=models.CASCADE, related_name='database_table', null=True, blank=True)
    column_name = models.CharField(max_length=255, verbose_name = "Database Column Name", related_name="column_name")
    data_type = models.CharField(max_length=255, verbose_name = "Data Type", related_name="data_type")
    is_nullable = models.BooleanField(default=False)
    is_primary_key = models.BooleanField(default=False)
    is_foreign_key = models.BooleanField(default=False)
    is_blankable = models.BooleanField(default=False)
    is_unique = models.BooleanField(default=False)
    is_indexed = models.BooleanField(default=False)
    is_auto_created = models.BooleanField(default=False)
    char_max_length = models.IntegerField(null=True, blank=True)
    numeric_precision = models.IntegerField(null=True, blank=True)
    slug = AutoSlugField(populate_from='table_name', unique=True)
    
    def __str__(self):
        return self.table_name