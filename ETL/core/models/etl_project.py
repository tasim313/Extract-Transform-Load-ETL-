from django.db import models
from autoslug import AutoSlugField
from .base import BaseModel
from .user import User

class ETLProject(BaseModel):
    name = models.CharField(max_length=255, verbose_name = "Name", related_name="name")
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='ProjectOwner',
        null=True,
        blank=True)
    
   
    def __str__(self):
        return self.name