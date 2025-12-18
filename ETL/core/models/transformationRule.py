from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .column_mapping import ColumnMapping

class TransformationRule(BaseModel):
    mapping = models.ForeignKey(ColumnMapping, on_delete=models.CASCADE, related_name='mapping', null=True, blank=True)
    rule_type = models.CharField(max_length=255, verbose_name="Rule", blank=True, null=True)
    rule_value = models.CharField(max_length=255, verbose_name="Rule Value", blank=True, null=True)
    slug = AutoSlugField(populate_from='table_name', unique=True)
    
    def __str__(self):
        return self.source_column + self.target_column