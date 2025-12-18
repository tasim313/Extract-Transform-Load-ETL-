from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .migration_job import MigrationJob


class JobSchedule(BaseModel):
    job = models.ForeignKey(MigrationJob, on_delete=models.CASCADE, related_name='migration_job', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    cron_expression = models.CharField(max_length=255, blank=True, null=True)
    next_run_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.run.job.name if self.run.job else f"MigrationRun ID: {self.pk}"