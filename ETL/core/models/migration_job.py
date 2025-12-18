from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .etl_project import ETLProject
from .etl_database_profile import ETLDatabaseProfile
from .enum import Status

class MigrationJob(BaseModel):
    project = models.ForeignKey(ETLProject, on_delete=models.CASCADE, related_name='project', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name = "Migration Job Name", related_name="name")
    description = models.TextField(blank=True, null=True)
    source_db = models.ForeignKey(ETLDatabaseProfile, on_delete=models.CASCADE, related_name='source_db', null=True, blank=True)
    target_db = models.ForeignKey(ETLDatabaseProfile, on_delete=models.CASCADE, related_name='target_db', null=True, blank=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING, verbose_name="Status")
    last_run_at = models.DateTimeField(auto_now_add=True)
    where_clause = models.TextField(blank=True, null=True)
    source_config = models.JSONField(default=dict,
        blank=True,
        null=True,
        help_text="Full source-side configuration (schema, tables, filters, column metadata).")
    target_config = models.JSONField(default=dict,
        blank=True,
        null=True,
        help_text="Full target-side configuration (schema, table mappings, column mappings).")
    resolved_mapping = models.JSONField(default=dict,
        blank=True,
        null=True,
        help_text="Auto-resolved, system-generated final column-to-column mapping.")
    slug = AutoSlugField(populate_from='table_name', unique=True)
    
    def __str__(self):
        return self.name