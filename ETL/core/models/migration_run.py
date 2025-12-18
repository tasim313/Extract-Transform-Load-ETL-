from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .migration_job import MigrationJob
from .enum import Status


class MigrationRun(models.Model):
    job = models.ForeignKey(MigrationJob, on_delete=models.CASCADE, related_name='job', null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING, verbose_name="Status")
    rows_extracted = models.IntegerField(null=True, blank=True)
    rows_loaded = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)
    artifacts_location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job.name if self.job else f"MigrationRun ID: {self.pk}"