from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .migration_run import MigrationRun
from .enum import Status


class MigrationErrorLog(BaseModel):
    run = models.ForeignKey(MigrationRun, on_delete=models.CASCADE, related_name='migration_run', null=True, blank=True)
    row_data = models.JSONField(default=dict,
        blank=True,
        null=True,
        help_text="Migration error log")
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.run.job.name if self.run.job else f"MigrationRun ID: {self.pk}"