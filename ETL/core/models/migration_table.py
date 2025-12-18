from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .migration_job import MigrationJob
from .database_schema import DatabaseSchema

class MigrationTable(BaseModel):
    job = models.ForeignKey(MigrationJob, on_delete=models.CASCADE, related_name='migration_job', null=True, blank=True)
    source_table = models.CharField(max_length=255, blank=True, null=True)
    db_source_schema = models.ForeignKey(DatabaseSchema, on_delete=models.CASCADE, related_name='db_source_schema', null=True, blank=True)
    target_table = models.CharField(max_length=255, blank=True, null=True)
    db_target_schema = models.ForeignKey(DatabaseSchema, on_delete=models.CASCADE, related_name='db_target_schema', null=True, blank=True)
    truncate_before_load = models.BooleanField(default=False)
    include_all_columns = models.BooleanField(default=False)
    def __str__(self):
        return self.job.name if self.run.job else f"MigrationRun ID: {self.pk}"