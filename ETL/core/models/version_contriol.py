from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .etl_project import ETLProject
from .version_control_repository import VersionControlRepository

class VersionedSnapshot(BaseModel):
    project = models.ForeignKey(ETLProject, on_delete=models.CASCADE, related_name='Project', null=True, blank=True)
    repository = models.ForeignKey(VersionControlRepository, on_delete=models.CASCADE, related_name='Repository', null=True, blank=True)
    commit_hash = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    snapshot_json = models.JSONField(default=dict, blank=True, null=True)
    change_summary = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.name