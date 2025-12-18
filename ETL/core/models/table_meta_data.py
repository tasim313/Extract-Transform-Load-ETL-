from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .etl_database_profile import ETLDatabaseProfile
from .database_schema import DatabaseSchema

class TableMetaData(BaseModel):
    db_profile = models.ForeignKey(ETLDatabaseProfile, on_delete=models.CASCADE, related_name='database_profile', null=True, blank=True)
    db_schema = models.ForeignKey(DatabaseSchema, on_delete=models.CASCADE, related_name='database_schema', null=True, blank=True)
    table_name = models.CharField(max_length=255, verbose_name = "Database Table Name", related_name="table_name")
    last_scanned = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='table_name', unique=True)
    
    def __str__(self):
        return self.table_name